import React, { useState, useEffect, useCallback, useRef } from 'react';
import { useAuth } from './contexts/AuthContext';
import './App.css';
import TodoDashboard from './components/TodoDashboard';
import FloatingChat from './components/FloatingChat';
import LoginForm from './components/LoginForm';
import RegisterForm from './components/RegisterForm';

function App() {
  const { user, token, loading, logout, getUserProfile } = useAuth();
  const [showAuth, setShowAuth] = useState('login'); // 'login', 'register', or null
  const [showChat, setShowChat] = useState(false); // For the floating chat
  const todoDashboardRef = useRef();

  // Check if user is logged in on initial load
  useEffect(() => {
    if (token && !user) {
      // If we have a token but no user info, fetch user profile
      const fetchUserProfile = async () => {
        try {
          // Use the auth context's getUserProfile function to update user state
          await getUserProfile();
        } catch (error) {
          console.error('Error fetching user profile:', error);
          logout();
        }
      };

      fetchUserProfile();
    }
  }, [token, user, logout, getUserProfile]);

  const handleLogout = () => {
    logout();
  };

  // Function to trigger task list refresh in TodoDashboard
  const refreshTasks = useCallback(async () => {
    // Call the fetchTasks function in TodoDashboard component
    if (todoDashboardRef.current && typeof todoDashboardRef.current.fetchTasks === 'function') {
      await todoDashboardRef.current.fetchTasks();
    }
  }, []);

  if (loading) {
    return <div className="App"><div className="loading">Loading...</div></div>;
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>AI Todo Assistant</h1>
        <p>Your personal AI assistant for managing tasks</p>
        {user && <p className="user-id">User: {user.username} ({user.email})</p>}
        {user && (
          <button onClick={handleLogout} className="logout-button">
            Logout
          </button>
        )}
      </header>
      <main>
        {!token ? (
          <div className="auth-section">
            {showAuth === 'login' ? (
              <LoginForm onSwitchToRegister={() => setShowAuth('register')} />
            ) : (
              <RegisterForm onSwitchToLogin={() => setShowAuth('login')} />
            )}
          </div>
        ) : (
          <>
            <TodoDashboard ref={todoDashboardRef} onRefresh={refreshTasks} />
            <FloatingChat
              isOpen={showChat}
              onOpen={() => setShowChat(true)}
              onClose={() => setShowChat(false)}
              onTaskUpdate={refreshTasks}
            />
          </>
        )}
      </main>
    </div>
  );
}

export default App;
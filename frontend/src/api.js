// api.js - API configuration
// Using full path to backend server to ensure API calls reach the backend
const API_BASE_URL = 'http://localhost:8000/api';

export default API_BASE_URL;

// Helper function to get user ID from auth context
// This would typically be called from components that have access to the auth context
export const getUserIdFromToken = (token) => {
  if (!token) return null;

  try {
    // Decode JWT token to extract user ID
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(
      atob(base64)
        .split('')
        .map(c => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
        .join('')
    );

    const decodedToken = JSON.parse(jsonPayload);
    return decodedToken.user_id || decodedToken.sub; // sub is commonly used for user ID in JWTs
  } catch (error) {
    console.error('Error decoding token:', error);
    return null;
  }
};
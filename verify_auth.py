import asyncio
import httpx
import json

async def test_registration():
    """Test the registration endpoint"""
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        # Prepare registration data
        user_data = {
            "email": "testuser2@example.com",
            "username": "testuser2",
            "password": "securepassword123"
        }
        
        print("Testing registration...")
        response = await client.post("/api/auth/register", json=user_data)
        
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Registration successful!")
            print(f"Response: {json.dumps(response.json(), indent=2)}")
            return response.json()
        else:
            print(f"Registration failed! Response: {response.text}")
            return None

async def test_login():
    """Test the login endpoint"""
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        # Prepare login data
        login_data = {
            "email": "testuser2@example.com",
            "password": "securepassword123"
        }
        
        print("\nTesting login...")
        response = await client.post("/api/auth/login", json=login_data)

        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Login successful!")
            print(f"Response: {json.dumps(response.json(), indent=2)}")
            return response.json()
        else:
            print(f"Login failed! Response: {response.text}")
            return None

async def test_get_profile(token):
    """Test retrieving user profile with token"""
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        headers = {"Authorization": f"Bearer {token}"}
        
        print("\nTesting profile retrieval...")
        response = await client.get("/api/auth/me", headers=headers)
        
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Profile retrieval successful!")
            print(f"Response: {json.dumps(response.json(), indent=2)}")
            return response.json()
        else:
            print(f"Profile retrieval failed! Response: {response.text}")
            return None

async def test_login_with_existing_user():
    """Test the login endpoint with the first test user"""
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        # Prepare login data for the first test user
        login_data = {
            "email": "test@example.com",
            "password": "securepassword123"
        }
        
        print("\nTesting login with existing user...")
        response = await client.post("/api/auth/login", json=login_data)

        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Login successful!")
            print(f"Response: {json.dumps(response.json(), indent=2)}")
            return response.json()
        else:
            print(f"Login failed! Response: {response.text}")
            return None

async def main():
    print("=== Testing Authentication Flow ===")
    
    # Test registration
    registration_result = await test_registration()
    
    # Test login with new user
    login_result_new = await test_login()
    
    # Test login with existing user
    login_result_existing = await test_login_with_existing_user()
    
    if login_result_existing and "access_token" in login_result_existing:
        # Test profile retrieval
        await test_get_profile(login_result_existing["access_token"])
    
    print("\n=== Authentication Flow Test Complete ===")

if __name__ == "__main__":
    asyncio.run(main())
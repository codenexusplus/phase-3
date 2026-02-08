import asyncio
import httpx
import json

async def test_registration():
    """Test the registration endpoint"""
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        # Prepare registration data
        user_data = {
            "email": "test@example.com",
            "username": "testuser",
            "password": "securepassword123"
        }

        print("Testing registration...")
        response = await client.post("/api/auth/register", json=user_data)

        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

        if response.status_code == 200:
            print("Registration successful!")
            return response.json()
        else:
            print("Registration failed!")
            return None

async def test_login():
    """Test the login endpoint"""
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        # Prepare login data
        login_data = {
            "email": "test@example.com",
            "password": "securepassword123"
        }

        print("\nTesting login...")
        response = await client.post("/api/auth/login", json=login_data)

        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

        if response.status_code == 200:
            print("Login successful!")
            return response.json()
        else:
            print("Login failed!")
            return None

async def test_get_profile(token):
    """Test retrieving user profile with token"""
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        headers = {"Authorization": f"Bearer {token}"}

        print("\nTesting profile retrieval...")
        response = await client.get("/api/auth/me", headers=headers)

        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

        if response.status_code == 200:
            print("Profile retrieval successful!")
            return response.json()
        else:
            print("Profile retrieval failed!")
            return None

async def main():
    # Test registration
    registration_result = await test_registration()
    
    # Test login
    login_result = await test_login()
    
    if login_result and "access_token" in login_result:
        # Test profile retrieval
        await test_get_profile(login_result["access_token"])

if __name__ == "__main__":
    asyncio.run(main())
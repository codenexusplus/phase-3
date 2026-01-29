import asyncio
import httpx
import json

async def test_chat_functionality():
    """Test the chat functionality with a simple message"""
    async with httpx.AsyncClient(base_url="http://localhost:8000") as client:
        # First, let's get a valid token by logging in
        print("Getting authentication token...")
        login_response = await client.post("/api/auth/login", json={
            "email": "test@example.com",
            "password": "securepassword123"
        })
        
        if login_response.status_code != 200:
            print(f"Failed to get token: {login_response.text}")
            return
            
        token_data = login_response.json()
        token = token_data["access_token"]
        user_id = token_data["user"]["id"]
        
        print(f"Got token for user {user_id}")
        
        # Now test the chat endpoint
        print("\nTesting chat endpoint...")
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        chat_data = {
            "message": "Hi, can you help me add a test task?",
            "conversation_id": None  # Will create a new conversation
        }
        
        response = await client.post("/api/chat", json=chat_data, headers=headers)
        
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            print("Chat endpoint working correctly!")
            response_json = response.json()
            print(f"Response keys: {list(response_json.keys())}")
            return response_json
        else:
            print("Chat endpoint failed!")
            return None

if __name__ == "__main__":
    result = asyncio.run(test_chat_functionality())
    if result:
        print(f"\nChat result keys: {list(result.keys())}")
        print(f"Action performed: {result.get('action_performed')}")
        print(f"Conversation ID: {result.get('conversation_id')}")
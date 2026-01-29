import jwt
import json
import base64
from datetime import datetime

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmMmE3OGYyZC1hYWM1LTRiNWItYWMzNy01MmZkMzhlMDY0OTciLCJleHAiOjE3Njk0NDI0NzV9.1-VOSzL7IhWMO0I1eiQuKNb9Y6G5c3UzXDzPBhDYMtU'

try:
    # Method 1: Using jwt library
    decoded = jwt.decode(token, options={'verify_signature': False})
    print('Token payload:', decoded)
    
    # Check expiration
    exp_timestamp = decoded.get('exp', 0)
    exp_datetime = datetime.fromtimestamp(exp_timestamp)
    current_datetime = datetime.now()
    
    print(f'Token expires at: {exp_datetime}')
    print(f'Current time: {current_datetime}')
    print(f'Token expired: {current_datetime > exp_datetime}')
    
except Exception as e:
    print(f'Error decoding token with jwt library: {e}')
    
    # Method 2: Manual decoding
    try:
        # Split the token
        header, payload, signature = token.split('.')
        
        # Decode the payload
        # Add padding if necessary
        payload += '=' * (4 - len(payload) % 4)
        decoded_payload = base64.b64decode(payload)
        payload_json = json.loads(decoded_payload)
        
        print('Manually decoded payload:', payload_json)
        
        # Check expiration
        exp_timestamp = payload_json.get('exp', 0)
        if exp_timestamp:
            exp_datetime = datetime.fromtimestamp(exp_timestamp)
            current_datetime = datetime.now()
            
            print(f'Token expires at: {exp_datetime}')
            print(f'Current time: {current_datetime}')
            print(f'Token expired: {current_datetime > exp_datetime}')
    except Exception as e2:
        print(f'Error with manual decoding: {e2}')
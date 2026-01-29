#!/usr/bin/env python3
"""
Script to start the backend server properly
"""

import sys
import os
import subprocess

def main():
    # Get the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Add the project root to Python path
    sys.path.insert(0, script_dir)

    # Change to the project directory
    os.chdir(script_dir)

    # Add the backend directory to Python path
    backend_dir = os.path.join(script_dir, 'backend')
    sys.path.insert(0, backend_dir)

    # Load environment variables from .env file
    from dotenv import load_dotenv
    backend_env_path = os.path.join(script_dir, 'backend', '.env')
    load_dotenv(dotenv_path=backend_env_path)

    # Import and run the app
    try:
        from backend.main_absolute import app
        import uvicorn

        print("Starting backend server on http://0.0.0.0:8000")
        uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)

    except ImportError as e:
        print(f"Import error: {e}")
        print("Make sure all dependencies are installed:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
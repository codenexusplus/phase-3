import sys
import os

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Change the working directory to the project root
os.chdir(project_root)

from backend.main import app
import uvicorn

if __name__ == "__main__":
    print("Starting backend server on http://0.0.0.0:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
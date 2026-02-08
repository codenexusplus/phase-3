import sys
import os
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Change working directory to project root
os.chdir(project_root)

# Now import and run the app
import uvicorn
from backend.main import app

if __name__ == "__main__":
    print("Starting backend server on http://0.0.0.0:8000")
    print("Press Ctrl+C to stop the server")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
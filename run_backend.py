import sys
import os

# Add the project root directory to the Python path
project_root = os.path.dirname(__file__)
sys.path.insert(0, project_root)

# Change the working directory to the project root
os.chdir(project_root)

from backend.main_absolute import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
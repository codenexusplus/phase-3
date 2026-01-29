from setuptools import setup, find_packages

setup(
    name="ai-todo-backend",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "sqlalchemy",
        "sqlmodel",
        "openai",
        "python-dotenv",
        "mcp",
    ],
)
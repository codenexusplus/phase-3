from fastapi import FastAPI
from contextlib import asynccontextmanager
from backend.api.chat_endpoint import router as chat_router
from backend.api.task_endpoint import router as task_router
from backend.config.settings import settings
from backend.database.connection import async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.middleware.cors import CORSMiddleware
import asyncio


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    # Initialize database tables if needed
    from models.user import User
    from models.task import Task
    from models.message import Message
    from models.conversation import Conversation
    from sqlalchemy import inspect
    import sqlite3

    # Create all tables
    async with async_engine.begin() as conn:
        await conn.run_sync(User.metadata.create_all)
        await conn.run_sync(Task.metadata.create_all)
        await conn.run_sync(Message.metadata.create_all)
        await conn.run_sync(Conversation.metadata.create_all)

    yield

    # Shutdown
    await async_engine.dispose()


app = FastAPI(
    title="AI Todo Agentic System",
    description="An AI-powered todo management system with natural language processing",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the chat router
app.include_router(chat_router, prefix="/api", tags=["chat"])

# Include the task router
app.include_router(task_router, prefix="/api", tags=["tasks"])

# Include the auth router
from backend.api.auth_endpoint import router as auth_router
app.include_router(auth_router, prefix="/api", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Todo Agentic System!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}
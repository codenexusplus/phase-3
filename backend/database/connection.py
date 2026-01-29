import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from urllib.parse import urlparse

# Load environment variables
load_dotenv()

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")

# Parse the URL to handle special parameters for asyncpg
parsed_url = urlparse(DATABASE_URL)

# Replace postgresql:// with postgresql+asyncpg:// if not already set
if DATABASE_URL.startswith("postgresql://"):
    # Extract components
    scheme = parsed_url.scheme.replace('postgresql', 'postgresql+asyncpg')
    username = parsed_url.username
    password = parsed_url.password
    hostname = parsed_url.hostname
    port = parsed_url.port or 5432  # Default PostgreSQL port
    database = parsed_url.path.lstrip('/')

    # Reconstruct URL without problematic query parameters for asyncpg
    DATABASE_URL = f"{scheme}://{username}:{password}@{hostname}:{port}/{database}"

    # If there are query parameters, we'll handle them separately if needed
    if parsed_url.query:
        # For Neon, we might need to handle SSL differently
        pass

# Create async engine
async_engine = create_async_engine(DATABASE_URL, echo=True)

# Create async session maker
AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=async_engine,
    class_=AsyncSession
)

def get_async_session():
    """Dependency to get async session"""
    async def async_session():
        async with AsyncSessionLocal() as session:
            yield session

    return async_session
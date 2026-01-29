# Quickstart Guide: AI Todo Agentic System

## Overview
This guide provides a quick way to get the AI Todo Agentic System up and running for development and testing purposes.

## Prerequisites
- Python 3.10 or higher
- pip package manager
- Access to OpenAI API (with appropriate API key)
- Access to Neon PostgreSQL database
- Node.js and npm (for frontend, if developing)

## Setup Steps

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Setup Your .env File
Create a file named `.env` in the root folder of the project:

```env
# Database
DATABASE_URL=postgresql://user:password@ep-your-db-id.us-east-2.aws.neon.tech/neondb?sslmode=require

# AI & Agents
OPENAI_API_KEY=sk-proj-your-key-here
OPENAI_DOMAIN_KEY=your-chatkit-domain-key

# Server Config
PORT=8000
DEBUG=True
```

### 3. Create Virtual Environment and Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Initialize the Database
```bash
# Run database migrations to create the required tables
python -m backend.database.migrate
```

### 5. Start the Backend Server
```bash
# Navigate to the backend directory
cd backend

# Start the FastAPI server
uvicorn main:app --reload --port 8000
```

### 6. (Optional) Start the Frontend
```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm start
```

## API Usage

### Chat Endpoint
Send a POST request to `/api/{user_id}/chat` with the following payload:

```json
{
  "message": "Add buy groceries to my tasks",
  "conversation_id": 1
}
```

The system will:
1. Authenticate the user_id
2. Fetch the last 10 messages from the conversation
3. Process the message with the AI agent
4. Execute any required MCP tools
5. Store the user message and AI response in the database
6. Return the AI's response

## Testing the System

### Natural Language Task Management
Try sending messages like:
- "Add buy milk to my tasks"
- "Show me my pending tasks"
- "Complete task #1"
- "Update task #2 to 'buy organic milk'"
- "Delete task #3"

### Conversation Memory
Start a conversation about a topic, then reference it later:
- "I have a project deadline next week"
- "Any updates?" (after adding some tasks)

## Troubleshooting

### Common Issues
1. **Database Connection Error**: Verify your DATABASE_URL in the .env file
2. **OpenAI API Error**: Check that your OPENAI_API_KEY is valid and has sufficient credits
3. **MCP Tools Not Working**: Ensure the MCP server is properly initialized and registered

### Logs
Check the server logs for detailed error messages. Enable DEBUG mode in your .env file for more verbose logging.

## Next Steps
- Explore the API documentation at `/docs` when the server is running
- Customize the agent's behavior by modifying the prompts in the agent configuration
- Extend the MCP tools to support additional functionality
- Integrate with your frontend application
# AI Todo Agentic System

An AI-powered todo management system that transforms a static Todo app into an Agentic System. The AI assistant understands natural language, manages tasks via MCP tools, and maintains long-term conversation memory.

## Features

- Natural language task management (create, read, update, delete tasks)
- Conversation memory and context awareness
- Secure user isolation (each user can only access their own tasks)
- MCP protocol compliance for all database operations
- Stateless architecture with persistent memory

## Tech Stack

- **Backend**: FastAPI (Python 3.10+)
- **AI Agent**: OpenAI Agents SDK
- **Protocol**: Official MCP Python SDK
- **Database**: SQLModel + Neon PostgreSQL (Async)
- **Frontend**: React with OpenAI ChatKit components

## Setup

### Backend Setup

1. Clone the repository
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and update with your credentials:
   ```bash
   cp .env.example .env
   # Edit .env with your actual values
   ```
5. Start the server:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

## Usage

The API endpoint is available at `/api/{user_id}/chat`. Send a POST request with the following JSON:

```json
{
  "message": "Add buy groceries to my tasks",
  "conversation_id": 1
}
```

The frontend provides a user-friendly chat interface to interact with the AI assistant.

## Architecture

The system enforces strict statelessness with every request cycle:
1. Authenticate the `user_id`
2. Retrieve conversation history from Neon DB
3. Execute the Agentic loop
4. Persist the new state back to DB

All database queries include a `WHERE user_id = :user_id` clause to ensure data isolation between users.

## MCP Tools

The system provides the following MCP tools for the AI agent:
- `add_task`: Creates a new task
- `list_tasks`: Lists tasks with optional status filter
- `complete_task`: Marks a task as completed
- `delete_task`: Deletes a task
- `update_task`: Updates task details

## Contributing

Contributions are welcome! Please follow the project's constitutional principles:
- Strict Statelessness
- MCP Protocol Compliance
- Technical Stack Standardization
- Coding & Naming Standards
- Natural Language Processing Capabilities
- Security & Privacy
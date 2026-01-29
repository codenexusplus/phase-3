---
id: 3
title: "Plan AI Todo Agentic System"
stage: plan
date: "2026-01-17"
surface: "agent"
model: "default"
feature: "001-ai-todo-agent"
branch: "001-ai-todo-agent"
user: "batool1"
command: "/sp.plan"
labels: ["planning", "architecture", "ai", "todo", "agent"]
links:
  spec: "specs/001-ai-todo-agent/spec.md"
  ticket: null
  adr: null
  pr: null
files_yaml:
  - "specs/001-ai-todo-agent/plan.md"
  - "specs/001-ai-todo-agent/research.md"
  - "specs/001-ai-todo-agent/data-model.md"
  - "specs/001-ai-todo-agent/quickstart.md"
  - "specs/001-ai-todo-agent/contracts/api-contract.md"
tests_yaml: []
---

# Prompt History Record

## Prompt Text

```
/sp.plan Implementation Plan: Phase III AI Todo Agentic System
Phase 1: Environment & Dependency Setup
[ ] Initialize a fresh Python virtual environment (python -m venv venv).

[ ] Create requirements.txt with:

fastapi, uvicorn (Backend)

sqlmodel, psycopg2-binary (Database)

mcp (Official MCP SDK)

openai-agents (OpenAI Agents SDK)

python-dotenv, pydantic-settings (Config)

[ ] Configure .env with DATABASE_URL, OPENAI_API_KEY, and OPENAI_DOMAIN_KEY.

Phase 2: Stateless Database Layer (SQLModel)
[ ] Implement backend/models.py:

TaskTable: id, user_id, title, description, completed, timestamps.

ConversationTable: id, user_id, created_at.

MessageTable: id, conversation_id, role (user/assistant), content, created_at.

[ ] Implement backend/database.py:

Setup Async Engine for Neon PostgreSQL.

Create get_session dependency.

Phase 3: MCP Server & Tool Definitions
[ ] Implement backend/mcp_server.py:

Initialize FastMCP or mcp.Server.

Register Tool: add_task (Validates via Pydantic).

Register Tool: list_tasks (Supports status filters).

Register Tool: update_task (Handles partial updates).

Register Tool: delete_task & complete_task.

[ ] Verification: Ensure all tools strictly filter by user_id.

Phase 4: Agentic Orchestration (The Brain)
[ ] Implement backend/agent_logic.py:

Initialize the OpenAI Agent.

Connect the MCP tools to the Agent.

[ ] Create a context-fetching helper:

get_conversation_context(conversation_id): Fetches last 10 messages from DB to maintain stateless memory.

Phase 5: FastAPI Endpoint & Stateless Cycle
[ ] Implement backend/main.py:

Endpoint: POST /api/{user_id}/chat.

Logic: 1. Receive message. 2. Fetch history from MessageTable. 3. Run Agent with history + MCP tools. 4. Save user input and agent output back to MessageTable. 5. Return JSON response.

Phase 6: Frontend Integration
[ ] Initialize OpenAI ChatKit in /frontend.

[ ] Map ChatKit's message handler to the FastAPI /chat endpoint.

[ ] Add domain allowlist configuration via environment variables.

How to Trigger the Build
Once you have saved this file, your final step is to give Claude Code the Execution Order:

"I have finalized the SDD files in /specs/. We are now in the IMPLEMENT stage.

Initialize the project based on plan.md.

Build the Database and MCP Tools first.

Connect the OpenAI Agent and ensure the /chat endpoint is fully stateless.

Use professional error handling as per the Constitution.

DO NOT stop until the backend is fully functional. PROCEED. also add Step 1: Setup Your .env File
Pehle ye file apne root folder mein banayein:

Code snippet

# Database
DATABASE_URL=postgresql://user:password@ep-your-db-id.us-east-2.aws.neon.tech/neondb?sslmode=require

# AI & Agents
OPENAI_API_KEY=sk-proj-your-key-here
OPENAI_DOMAIN_KEY=your-chatkit-domain-key

# Server Config
PORT=8000
DEBUG=True
Step 2: The Master Build Prompt
Ab Claude Code terminal mein ye poora prompt paste karein:

"Act as a Senior AI Solutions Architect. I am building Phase III of my Todo System as a standalone, professional Agentic Application. Follow the Spec-Driven Development (SDD) workflow strictly.

Project Context: I have prepared the following files in the /specs folder:

.sp.constitution: Defines the 'Law of the Land' (Statelessness, Async, Naming).

system_spec.md: Defines the Intent, DB Models, and MCP Tool signatures.

plan.md: Defines the Atomic tasks for implementation.

Core Technical Requirements:

Language: Python 3.10+ (FastAPI).

Brain: OpenAI Agents SDK (Agent + Runner pattern).

Tools: Official MCP Python SDK (to handle Task CRUD).

Database: SQLModel + Neon Postgres (Async).

History: Every /chat request must fetch the last 10 messages from the DB to inject context into the Agent (Stateless Recall).

Your Instructions:

Initialize: Read all files in /specs/ to align with the project's 'Constitution'.

Implementation Order:

Create backend/models.py (Task, Conversation, Message tables).

Create backend/database.py (Async session & engine).

Create backend/mcp_server.py (Tools for Add/List/Complete/Update/Delete).

Create backend/agent_logic.py (OpenAI Agent orchestration with history injection).

Create backend/main.py (FastAPI router with /api/{user_id}/chat).

Standard: Ensure every database operation is scoped by user_id. Use Pydantic V2 for all data validations.

Output: Build the entire backend in one-shot. Verify that the agent can remember past messages and successfully execute MCP tools based on user intent.

The .env is already provided in the root. DO NOT stop until the system is fully functional. PROCEED."
```

## Response Text

Completed the implementation planning for the AI Todo Agentic System. Created the following artifacts:

1. Implementation plan (plan.md) detailing the architecture and structure
2. Research document (research.md) resolving all technical unknowns
3. Data model (data-model.md) defining the database schema
4. Quickstart guide (quickstart.md) for easy setup
5. API contracts (contracts/api-contract.md) defining the interfaces
6. Updated agent context in QWEN.md

The plan ensures constitutional compliance with:
- Strict statelessness
- MCP Protocol compliance
- Technical stack standardization
- Coding and naming standards
- Natural language processing capabilities
- Security and privacy requirements

## Outcome

Successfully created a comprehensive implementation plan for the AI Todo Agentic System that aligns with the project constitution and feature specification. All required artifacts have been generated and the agent context has been updated.

## Evaluation

The plan addresses all requirements from the feature specification while maintaining compliance with the constitutional principles. The architecture is well-defined with proper separation of concerns, and all necessary documentation has been created to support the implementation phase.
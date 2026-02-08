---
id: 1
title: "Update project constitution"
stage: constitution
date: "2026-01-17"
surface: "agent"
model: "default"
feature: "none"
branch: "main"
user: "batool1"
command: "/sp.constitution"
labels: ["constitution", "governance", "setup"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - ".specify/memory/constitution.md"
tests_yaml: []
---

# Prompt History Record

## Prompt Text

```
/sp.constitution # Phase III: AI Todo Chatbot - System Constitution

## 1. Architectural Mandate
- **Strict Statelessness:** The FastAPI server must not hold any in-memory state. Every request cycle must:
    1. Authenticate the `user_id`.
    2. Retrieve conversation history from Neon DB.
    3. Execute the Agentic loop.
    4. Persist the new state back to DB.
- **MCP Protocol:** All business logic for Task CRUD must be encapsulated within an Official MCP Server. The AI Agent must interact with the DB *only* through these MCP tools.

## 2. Technical Stack & Skills
- **Runtime:** Python 3.10+ (FastAPI)
- **Agentic Framework:** OpenAI Agents SDK (using Agent + Runner patterns).
- **Tooling Protocol:** Official MCP Python SDK.
- **ORM & Database:** SQLModel with Neon Serverless PostgreSQL (Async Engine).
- **Validation:** Pydantic V2 for all schemas and tool parameters.
- **Communication:** Asynchronous (async/await) throughout the entire stack.

## 3. Coding & Naming Standards
- **Naming:** - Classes: `PascalCase`
    - Functions/Variables: `snake_case`
    - Constants: `UPPER_SNAKE_CASE`
- **Error Handling:** Use structured exceptions. Tools must return clear error messages (e.g., "Task ID {id} not found") so the Agent can explain the issue to the user.
- **Type Hinting:** Mandatory type hints for all function signatures.

## 4. Skills & Capabilities
- **Context Injection:** The system must implement a 'Last-N Messages' sliding window (default: 10) for conversation context.
- **Natural Language Understanding (NLU):** The agent must handle ambiguous commands (e.g., "Remind me to buy milk" -> `add_task`).
- **Confirmation Flow:** The Agent must use formatted Markdown to confirm actions (e.g., "✅ **Task Added:** Buy groceries").

## 5. Security & Privacy
- **Tenancy:** Every SQL query must include a `WHERE user_id = :user_id` clause to prevent data leakage between users.
- **Secret Management:** Sensitive keys (OpenAI, Neon URL) must be read from environment variables only.
```

## Response Text

Updated the project constitution file at `.specify/memory/constitution.md` with the specified principles for the AI Todo Chatbot project. The new constitution includes sections on architectural mandate, technical stack, coding standards, skills/capabilities, and security requirements. Also performed checks on related template files to ensure alignment with the new constitution.

## Outcome

Successfully created a comprehensive constitution document for the AI Todo Chatbot project that outlines the core principles, constraints, and governance guidelines. The constitution will serve as the authoritative reference for all future development decisions.

## Evaluation

The constitution has been properly created with all the specified principles. The document follows the required format and includes all necessary sections as outlined in the user's request. Template files were checked for alignment, and a proper version control header was added to the constitution file.
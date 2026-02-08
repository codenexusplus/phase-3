# API Contract: AI Todo Agentic System

## Overview
This document defines the API contracts for the AI Todo Agentic System based on the functional requirements in the feature specification.

## Base URL
`https://your-domain.com/api`

## Authentication
All endpoints require user identification via the `user_id` path parameter. The system implements user isolation through database queries that include `WHERE user_id = :user_id`.

## Endpoints

### POST /{user_id}/chat
Initiates or continues a conversation with the AI assistant.

#### Request
```json
{
  "message": "Add buy groceries to my tasks",
  "conversation_id": 1
}
```

#### Response
```json
{
  "response": "✅ **Task Added:** Buy groceries",
  "conversation_id": 1,
  "timestamp": "2026-01-17T10:30:00Z"
}
```

#### Error Response
```json
{
  "error": "Task not found",
  "message": "The requested operation could not be completed"
}
```

#### Functional Requirements Mapped
- FR-001: System interprets natural language user inputs
- FR-002: User can create new tasks via natural language
- FR-003: User can view tasks via natural language
- FR-004: User can mark tasks as completed via natural language
- FR-005: User can delete tasks via natural language
- FR-006: User can update task details via natural language
- FR-007: System maintains conversation history
- FR-010: System provides clear confirmation messages
- FR-011: System handles error cases gracefully
- FR-012: System ensures data isolation by user

### GET /{user_id}/tasks
Retrieves the user's tasks with optional filtering.

#### Query Parameters
- `status` (optional): Filter by task status ('all', 'pending', 'completed')

#### Response
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Buy groceries",
      "description": "Milk, bread, eggs",
      "completed": false,
      "created_at": "2026-01-17T09:00:00Z",
      "updated_at": "2026-01-17T09:00:00Z"
    }
  ]
}
```

#### Functional Requirements Mapped
- FR-003: User can view tasks filtered by status
- FR-012: System ensures data isolation by user

### POST /{user_id}/tasks
Creates a new task.

#### Request
```json
{
  "title": "Buy groceries",
  "description": "Milk, bread, eggs"
}
```

#### Response
```json
{
  "task": {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, bread, eggs",
    "completed": false,
    "created_at": "2026-01-17T09:00:00Z",
    "updated_at": "2026-01-17T09:00:00Z"
  }
}
```

#### Functional Requirements Mapped
- FR-002: User can create new tasks
- FR-012: System ensures data isolation by user

### PUT /{user_id}/tasks/{task_id}
Updates an existing task.

#### Request
```json
{
  "title": "Buy organic groceries",
  "description": "Organic milk, whole grain bread, free-range eggs"
}
```

#### Response
```json
{
  "task": {
    "id": 1,
    "title": "Buy organic groceries",
    "description": "Organic milk, whole grain bread, free-range eggs",
    "completed": false,
    "created_at": "2026-01-17T09:00:00Z",
    "updated_at": "2026-01-17T10:00:00Z"
  }
}
```

#### Functional Requirements Mapped
- FR-006: User can update task details
- FR-012: System ensures data isolation by user

### DELETE /{user_id}/tasks/{task_id}
Deletes a task.

#### Response
```json
{
  "success": true,
  "message": "Task deleted successfully"
}
```

#### Functional Requirements Mapped
- FR-005: User can delete tasks
- FR-012: System ensures data isolation by user

### POST /{user_id}/tasks/{task_id}/complete
Marks a task as completed.

#### Response
```json
{
  "task": {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, bread, eggs",
    "completed": true,
    "created_at": "2026-01-17T09:00:00Z",
    "updated_at": "2026-01-17T10:30:00Z"
  }
}
```

#### Functional Requirements Mapped
- FR-004: User can mark tasks as completed
- FR-012: System ensures data isolation by user

## MCP Tool Contracts

### add_task(user_id, title, description)
Creates a new entry in the Tasks table.

#### Parameters
- `user_id`: Identifier for the user
- `title`: Title of the task
- `description`: Description of the task

#### Returns
- `task_id`: ID of the newly created task

#### Functional Requirements Mapped
- FR-002: System allows users to create new tasks

### list_tasks(user_id, status)
Filters tasks by 'all', 'pending', or 'completed'.

#### Parameters
- `user_id`: Identifier for the user
- `status`: Filter status ('all', 'pending', 'completed')

#### Returns
- Array of task objects matching the criteria

#### Functional Requirements Mapped
- FR-003: System allows users to view their tasks filtered by status

### complete_task(user_id, task_id)
Marks a specific task as done.

#### Parameters
- `user_id`: Identifier for the user
- `task_id`: ID of the task to complete

#### Returns
- Boolean indicating success or failure

#### Functional Requirements Mapped
- FR-004: System allows users to mark tasks as completed

### delete_task(user_id, task_id)
Permanently removes a task.

#### Parameters
- `user_id`: Identifier for the user
- `task_id`: ID of the task to delete

#### Returns
- Boolean indicating success or failure

#### Functional Requirements Mapped
- FR-005: System allows users to delete tasks

### update_task(user_id, task_id, title, description)
Modifies existing task details.

#### Parameters
- `user_id`: Identifier for the user
- `task_id`: ID of the task to update
- `title`: New title for the task
- `description`: New description for the task

#### Returns
- Boolean indicating success or failure

#### Functional Requirements Mapped
- FR-006: System allows users to update task details

## Error Handling
All endpoints follow the same error response format:
```json
{
  "error": "Error message",
  "code": "ERROR_CODE"
}
```

## Security
- All database queries must include WHERE user_id = :user_id clause
- API keys must be stored in environment variables
- All sensitive data must be handled securely
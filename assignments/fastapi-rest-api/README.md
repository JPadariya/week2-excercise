# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build RESTful APIs using the FastAPI framework, practicing HTTP methods, data validation, and JSON responses.

## 📝 Tasks

### 🛠️	Create a Basic API Server

#### Description
Set up a FastAPI application with basic endpoints for creating, reading, updating, and deleting items.

#### Requirements
Completed program should:

- Install FastAPI and uvicorn for running the server
- Create GET endpoint to retrieve all items from a list
- Create POST endpoint to add a new item with validation
- Create PUT endpoint to update an existing item by ID
- Create DELETE endpoint to remove an item by ID


### 🛠️	Implement Data Models and Validation

#### Description
Use Pydantic models to validate incoming request data and structure API responses.

#### Requirements
Completed program should:

- Define a Pydantic model for the item with required fields (id, name, description, price)
- Validate that price is a positive number
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Handle errors gracefully with proper error messages
- Test all endpoints using the automatic FastAPI documentation at `/docs`

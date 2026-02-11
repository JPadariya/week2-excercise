"""
FastAPI REST API Starter Code
Complete the TODO items to build a functional REST API
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(title="Items API", description="A simple REST API for managing items")

# TODO: Define your Pydantic model for Item
# Hint: Include fields for id, name, description, and price
class Item(BaseModel):
    pass


# In-memory storage (replace with database in production)
items_db: List[Item] = []
next_id = 1


@app.get("/")
def root():
    """Welcome endpoint"""
    return {"message": "Welcome to the Items API! Visit /docs for the interactive documentation."}


# TODO: Implement GET /items - Retrieve all items
@app.get("/items")
def get_items():
    pass


# TODO: Implement POST /items - Create a new item
@app.post("/items", status_code=201)
def create_item(item: Item):
    pass


# TODO: Implement GET /items/{item_id} - Retrieve a specific item by ID
@app.get("/items/{item_id}")
def get_item(item_id: int):
    pass


# TODO: Implement PUT /items/{item_id} - Update an item by ID
@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    pass


# TODO: Implement DELETE /items/{item_id} - Delete an item by ID
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    pass


# Run with: uvicorn starter-code:app --reload

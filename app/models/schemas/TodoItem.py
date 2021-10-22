from typing import List

from pydantic import BaseModel

from models.domain.TodoItem import TodoItem


class TodoItemInCreate(BaseModel):
    name: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Walk the dog"
            }
        }


class TodoItemInResponse(BaseModel):
    item: TodoItem

    class Config:
        schema_extra = {
            "example": {
                "item": {
                    "id": 1,
                    "name": "Walk the dog",
                    "is_completed": False,
                    "owner_id": "933ad738-7265-4b5f-9eae-a1a62928772e"
                }
            }
        }


class TodoItemsInList(BaseModel):
    items: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "items": [
                    {
                        "id": 1,
                        "name": "Walk the dog",
                        "is_completed": False,
                        "owner_id": "933ad738-7265-4b5f-9eae-a1a62928772e"
                    },
                    {
                        "id": 2,
                        "name": "Feed the cat",
                        "is_completed": False,
                        "owner_id": "933ad738-7265-4b5f-9eae-a1a62928772e"
                    },
                ]
            }
        }

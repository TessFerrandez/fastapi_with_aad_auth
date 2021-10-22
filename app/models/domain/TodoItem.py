from pydantic import BaseModel


class TodoItem(BaseModel):
    id: int
    owner_id: str
    name: str
    is_complete: bool

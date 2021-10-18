from typing import List

from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    owner: str


class ItemsInList(BaseModel):
    items: List[Item]

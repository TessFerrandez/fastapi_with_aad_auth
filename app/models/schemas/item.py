from typing import List
from pydantic import BaseModel

from app.models.domain.item import Item


class ItemInCreate(BaseModel):
    name: str


class ItemInResponse(BaseModel):
    item: Item


class ItemsInList(BaseModel):
    items: List[Item]

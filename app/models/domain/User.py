from typing import List

from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str
    preferred_username: str
    roles: List[str]

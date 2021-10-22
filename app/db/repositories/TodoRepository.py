from typing import Dict, List

from db.exceptions import EntityNotFound
from models.domain.TodoItem import TodoItem
from models.domain.User import User
from models.schemas.TodoItem import TodoItemInCreate



class TodoRepository():
    def __init__(self) -> None:
        self.max_index: int = 0
        self.fake_db: Dict[int, TodoItem] = {}

    def create_item(self, todo_create: TodoItemInCreate, user: User) -> TodoItem:
        self.max_index += 1
        todo = TodoItem(id=self.max_index, name=todo_create.name, owner_id=user.id, is_complete=False)
        self.fake_db[self.max_index] = todo
        return todo

    def delete_all_items(self) -> None:
        self.fake_db.clear()
        self.max_index = 0

    def delete_item(self, id: int) -> None:
        if id not in self.fake_db:
            raise EntityNotFound
        del self.fake_db[id]

    def get_items_for_user(self, user: User) -> List[TodoItem]:
        if 'Admin' in user.roles:
            return [todo for todo in self.fake_db.values()]
        else:
            return [todo for todo in self.fake_db.values() if todo.owner_id == user.id]

    def get_item(self, id: int) -> TodoItem:
        if id not in self.fake_db:
            raise EntityNotFound
        return self.fake_db[id]


todo_repository = TodoRepository()

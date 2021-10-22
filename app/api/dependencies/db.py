from fastapi import Depends, Path
from fastapi import HTTPException, status

from api.dependencies.auth import get_user
from db.exceptions import EntityNotFound
from db.repositories.TodoRepository import todo_repository
from models.domain.User import User
from models.domain.TodoItem import TodoItem


def get_todo_item_by_id_from_path(id: int = Path(...), user: User = Depends(get_user)):
    try:
        todo: TodoItem = todo_repository.get_item(id)
    except EntityNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item does not exist')

    if 'Admin' in user.roles or todo.owner_id == user.id:
        return todo
    raise HTTPException(status.HTTP_403_FORBIDDEN, detail='User is not allowed to access the item')

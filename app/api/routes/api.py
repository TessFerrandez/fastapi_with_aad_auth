from typing import List

from fastapi import APIRouter, Body, Depends, status

from api.dependencies.db import get_todo_item_by_id_from_path
from api.dependencies.auth import get_user, get_admin_user
from db.repositories.TodoRepository import todo_repository
from models.domain.TodoItem import TodoItem
from models.domain.User import User
from models.schemas.TodoItem import TodoItemInCreate, TodoItemInResponse, TodoItemsInList


router = APIRouter()


# no authentication needed
@router.get('/health', status_code=status.HTTP_200_OK, name="Get Health Status [NO AUTH REQUIRED]")
async def get_health_status():
    return 'OK'


# requires user to be authenticated, only returns items for this user, or all for admin
# that the user is authenticated is verified by Depends(get_user)
@router.get('/todoitems', status_code=status.HTTP_200_OK, name="Get My Todos [Admin or Owner of todo]")
async def get_my_todos(user: User = Depends(get_user)) -> TodoItemsInList:
    items: List[TodoItem] = todo_repository.get_items_for_user(user)
    return TodoItemsInList(items=items)


# requires user to be authenticated
# that the user is authenticated is verified by Depends(get_user)
@router.post('/todoitems', status_code=status.HTTP_201_CREATED, name="Create Todo [User]")
async def create_todo(todo_create: TodoItemInCreate = Body(..., embed=True, alias="item"), user: User = Depends(get_user)) -> TodoItemInResponse:
    todo: TodoItem = todo_repository.create_item(todo_create, user)
    return TodoItemInResponse(item=todo)


# requires user to be admin
# note how we don't need to know who the user is, only that they are admin, so we can add this to the decorator
@router.delete('/todoitems', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(get_admin_user)], name="Delete all Todos [Admin]")
async def delete_all_todo_items() -> None:
    todo_repository.delete_all_items()


# requires user to be authenticated and owner of item (or admin)
# This is verified in the get_todo_item_by_id_from_path dependency
@router.get('/todoitems/{id}', status_code=status.HTTP_200_OK, name="Get Todo by Id [Admin or Owner of todo]")
async def get_todo_by_id(id: int, todo: TodoItem = Depends(get_todo_item_by_id_from_path)) -> TodoItemInResponse:
    return TodoItemInResponse(item=todo)


# requires user to be authenticated and owner of item (or admin)
# This is verified in the get_todo_item_by_id_from_path dependency
@router.delete('/todoitems/{id}', status_code=status.HTTP_204_NO_CONTENT, name="Delete Todo [Admin or Owner of todo]")
async def delete_todo(id: int, todo: TodoItem = Depends(get_todo_item_by_id_from_path)) -> None:
    todo_repository.delete_item(todo.id)

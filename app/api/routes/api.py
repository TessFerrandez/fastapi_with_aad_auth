from typing import List

from fastapi import APIRouter, Body, Depends, status
from fastapi.exceptions import HTTPException

from app.models.domain.item import Item
from app.models.schemas.item import ItemInCreate, ItemInResponse, ItemsInList


router = APIRouter()


# no authentication needed
@router.get('/health', status_code=status.HTTP_200_OK)
async def get_health_status():
    return 'OK'


# requires user to be authenticated, only returns items for this user, or all for admin
@router.get('/items', status_code=status.HTTP_200_OK)
async def get_my_items(repo: ItemsRepo = Depends(get_repo(ItemsRepo)), user: User = Depends(Authenticate[roles=['Admin', 'User']])) -> ItemsInList:
    items: List[Item] = repo.get_items_for_user(user)
    return ItemsInList(items=items)


# requires user to be authenticated and owner of item
@router.get('/items/{id}', status_code=status.HTTP_200_OK)
async def get_item(item: Item = Depends(get_item_by_id_from_path), user: User = Depends(Authenticate[roles=['Admin', 'User']])) -> ItemInResponse:
    if user.role == 'Admin' or item.owner == user.id:
        return ItemInResponse(item=item)
    raise HTTPException(status.HTTP_403_FORBIDDEN, detail=strings.USER_IS_NOT_OWNER_OF_ITEM)


# requires user to be authenticated
@router.post('/items', status_code=status.HTTP_201_CREATED)
async def create_item(item_create: ItemInCreate = Body(..., embed=True, alias="item"), repo: ItemsRepo = Depends(get_repo(ItemsRepo)), user: User = Depends(Authenticate[roles=['Admin', 'User']])) -> ItemInResponse:
    item: Item = repo.create_item(item_create)
    return ItemInResponse(item=item)


# requires user to be admin
@router.delete('/items/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item: Item = Depends(get_item_by_id_from_path), repo: ItemsRepo = Depends(get_repo(ItemsRepo)), user: User = Depends(Authenticate[roles=['Admin']])) -> None:
    repo.delete_item(item.id)

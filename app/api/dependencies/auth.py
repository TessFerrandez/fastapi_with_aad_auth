from typing import Any

from fastapi import Depends, HTTPException, status

from models.domain.User import User


class ForbiddenAccess(HTTPException):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail, headers={"WWW-Authenticate": "Bearer"})


def get_user() -> User:
    return User(id='123', name='Test', preferred_username='Test', roles=['Admin'])


def get_admin_user(user: User = Depends(get_user)) -> User:
    if 'Admin' in user.roles:
        return user
    raise ForbiddenAccess('Admin privileges required')

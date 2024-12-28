from fastapi import APIRouter
from users.models import UserCreate, UserUpdate, UserPublic
from users import crud
from core.db import SessionDep

#Тут обозначаются эндпоинты, которые
# передают запросы в CRUD возвращают то что надо

router = APIRouter()


@router.post("/", response_model=UserPublic)
def create_user(user: UserCreate, session: SessionDep):
    return crud.create_user(user, session)


@router.get("/{user_id}/", response_model=UserPublic)
def get_user(user_id: int, session: SessionDep):
    return crud.get_user(user_id, session)


@router.get("/", response_model=list[UserPublic])
def get_users(session: SessionDep):
    return crud.get_users(session)


@router.patch("/{user_id}/", response_model=UserPublic)
def update_user(user_id: int, user: UserUpdate, session: SessionDep):
    return crud.update_user(user_id, user, session)


@router.delete("/{user_id}/")
def delete_user(user_id: int, session: SessionDep):
    return crud.delete_user(user_id, session)

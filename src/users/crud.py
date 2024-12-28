from sqlmodel import select, Session
from fastapi import HTTPException
from models import User, UserCreate, UserUpdate


def create_user(user: UserCreate, session: Session):
    db_user = User.model_validate(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def get_user(user_id: int, session: Session):
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


def get_users(session: Session):
    db_users = session.exec(select(User)).all()
    return db_users


def update_user(user_id: int, user: UserUpdate, session: Session):
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = user.model_dump(exclude_unset=True)
    db_user.sqlmodel_update(user_data)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def delete_user(user_id: int, session: Session):
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(db_user)
    session.commit()
    return {"result": True}

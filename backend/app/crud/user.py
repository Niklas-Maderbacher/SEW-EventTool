from sqlalchemy.orm import Session
from app.models.user import User
from app.models.user_roles import USER_ROLE
from app.schemas.user import UserCreate, UserBase, UserUpdate, UserInDB
from app.core.security import get_password_hash, verify_password
from app.crud.exeptions.not_authorised import UserNotAuthorised

from datetime import datetime, timezone


def create_user(*, db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        email=user.email,
        phone_number=user.phone_number,
        password_hash=get_password_hash(user.password),
        role=user.role,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_id(*, db: Session, user_id: int, user: UserInDB):
    if user.role != USER_ROLE.ADMIN or user.id != user_id:
        raise UserNotAuthorised()
    else:
        return db.query(User).filter(User.id == user_id).first()

def get_user_by_name(*, db: Session, name: str):
    return db.query(User).filter(User.name == name).first()

def get_user_by_email(*, db: Session, email: str, user: UserInDB):
    return db.query(User).filter(User.email == email).first()

def get_user_by_role(*, db: Session, role: USER_ROLE, user: UserInDB):
    if user.role != USER_ROLE.ADMIN:
        raise UserNotAuthorised()
    else:
        return db.query(User).filter(User.role == role).all()


def get_users(*, db: Session):
    return db.query(User).all()


def authenticate_user(*, db: Session, name: str, password: str):
    db_user = db.query(User).filter(User.name == name).first()
    if not db_user:
        return None
    if not verify_password(password, str(db_user.password_hash)):
        return None
    return db_user

def update_user(*, db: Session, user_update: UserUpdate, user: UserInDB):
    user_db = db.query(User).filter(User.id == user.id).first()

    user_db.name = user_update.name
    user_db.email = user_update.email
    user_db.phone_number = user_update.phone_number
    user_db.role = user_update.role

    db.commit()
    db.refresh(user_db)

    return user_db

def delete_user(*, db: Session, user: UserInDB):
    user_db = db.query(User).filter(User.email == user.email).first()

    db.query(User).filter(User.email == user.email).delete()
    db.commit()

    return user_db

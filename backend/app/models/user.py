from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import Enum as SQL_ENUM
from datetime import datetime

from app.database.session import Base
from app.models.user_roles import USER_ROLE


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(15), unique=True, index=True, nullable=False)
    email = Column(String(50), unique=True, index=True, nullable=False)
    phone_number = Column(String(50), unique=True, nullable=True)
    password_hash = Column(String, nullable=False)
    role = Column(SQL_ENUM(USER_ROLE), nullable=False)

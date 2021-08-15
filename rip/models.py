from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Boolean, String, Column, Table, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String(128), index=True, unique=True, nullable=False)
    hashed_password = Column(String(512), nullable=False)
    full_name = Column(String(128), nullable=False)

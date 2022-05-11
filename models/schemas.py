from typing import List
from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str


class TodoCreate(TodoBase):
    completed: bool


class Todo(TodoBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    todo: List[Todo] = []

    class Config:
        orm_mode = True

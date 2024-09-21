from pydantic import BaseModel
from typing import List, Optional

# Esquema para criar um novo usuário
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    active: Optional[bool] = True

# Esquema para atualizar um usuário
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    active: Optional[bool] = None

# Esquema de resposta do usuário (inclui o ID e livros)
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    active: bool
    books: List['BookResponse'] = []  # Lista de livros associados ao usuário

    class Config:
        from_attributes = True  # Atualização aqui

# Esquema para criar um novo livro
class BookCreate(BaseModel):
    title: str
    pages: int
    writer: int  # O ID do autor (usuário)

# Esquema para atualizar um livro
class BookUpdate(BaseModel):
    title: Optional[str] = None
    pages: Optional[int] = None

# Esquema de resposta do livro (inclui o ID e o autor)
class BookResponse(BaseModel):
    id: int
    title: str
    pages: int
    writer: int

    class Config:
        from_attributes = True  # Atualização aqui

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models
import schemas
from repositories import UserRepository, BookRepository
from typing import List

engine = create_engine("sqlite:///meubanco.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------------------- #
# Endpoints CRUD para User
# ------------------------------- #

@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    return user_repo.create_user(user.name, user.email, user.password, user.active)

@app.get("/users/", response_model=List[schemas.UserResponse])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    return user_repo.get_users(skip, limit)

@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    return user_repo.get_user(user_id)

@app.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    return user_repo.update_user(user_id, user.name, user.email, user.password, user.active)

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    user_repo.delete_user(user_id)
    return {"detail": "Usuário deletado com sucesso"}

# ------------------------------- #
# Endpoints CRUD para Book
# ------------------------------- #

@app.post("/books/", response_model=schemas.BookResponse)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    book_repo = BookRepository(db)
    return book_repo.create_book(book.title, book.pages, book.writer)

@app.get("/books/", response_model=List[schemas.BookResponse])
def get_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    book_repo = BookRepository(db)
    return book_repo.get_books(skip, limit)

@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book_repo = BookRepository(db)
    return book_repo.get_book(book_id)

@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    book_repo = BookRepository(db)
    return book_repo.update_book(book_id, book.title, book.pages)

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_repo = BookRepository(db)
    book_repo.delete_book(book_id)
    return {"detail": "Livro deletado com sucesso"}

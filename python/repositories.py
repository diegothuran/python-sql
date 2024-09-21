from sqlalchemy.orm import Session
from models import User, Book
from fastapi import HTTPException

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, name: str, email: str, password: str, active: bool = True):
        db_user = self.db.query(User).filter(User.email == email).first()
        if db_user:
            raise HTTPException(status_code=400, detail="Email já registrado")
        new_user = User(name=name, email=email, password=password, active=active)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def get_users(self, skip: int = 0, limit: int = 10):
        return self.db.query(User).offset(skip).limit(limit).all()

    def get_user(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return user

    def update_user(self, user_id: int, name: str = None, email: str = None, password: str = None, active: bool = None):
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if not db_user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        if name:
            db_user.name = name
        if email:
            db_user.email = email
        if password:
            db_user.password = password
        if active is not None:
            db_user.active = active
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int):
        db_user = self.db.query(User).filter(User.id == user_id).first()
        if not db_user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        self.db.delete(db_user)
        self.db.commit()

class BookRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_book(self, title: str, pages: int, writer: int):
        db_user = self.db.query(User).filter(User.id == writer).first()
        if not db_user:
            raise HTTPException(status_code=400, detail="Autor não encontrado")
        new_book = Book(title=title, pages=pages, writer=writer)
        self.db.add(new_book)
        self.db.commit()
        self.db.refresh(new_book)
        return new_book

    def get_books(self, skip: int = 0, limit: int = 10):
        return self.db.query(Book).offset(skip).limit(limit).all()

    def get_book(self, book_id: int):
        book = self.db.query(Book).filter(Book.id == book_id).first()
        if not book:
            raise HTTPException(status_code=404, detail="Livro não encontrado")
        return book

    def update_book(self, book_id: int, title: str = None, pages: int = None):
        db_book = self.db.query(Book).filter(Book.id == book_id).first()
        if not db_book:
            raise HTTPException(status_code=404, detail="Livro não encontrado")
        if title:
            db_book.title = title
        if pages:
            db_book.pages = pages
        self.db.commit()
        self.db.refresh(db_book)
        return db_book

    def delete_book(self, book_id: int):
        db_book = self.db.query(Book).filter(Book.id == book_id).first()
        if not db_book:
            raise HTTPException(status_code=404, detail="Livro não encontrado")
        self.db.delete(db_book)
        self.db.commit()

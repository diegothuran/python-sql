from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

# Definindo o Base
Base = declarative_base()

# Classe User (Tabela 'users')
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    active = Column(Boolean, default=True)

    # Relacionamento com a tabela Book
    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")

# Classe Book (Tabela 'books')
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    pages = Column(Integer, nullable=False)
    writer = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relacionamento com a tabela User
    author = relationship("User", back_populates="books")

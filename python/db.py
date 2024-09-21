from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import os

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()


# Tabela de usuários
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    active = Column(Boolean, default=True)

    # Relacionamento com a tabela de livros
    books = relationship("Book", back_populates="author")


# Tabela de livros
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    pages = Column(Integer, nullable=False)
    writer = Column(Integer, ForeignKey("users.id"))

    # Relacionamento com a tabela de usuários
    author = relationship("User", back_populates="books")


# Criação das tabelas no banco de dados
Base.metadata.create_all(bind=db)

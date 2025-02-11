from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql.schema import ForeignKey
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    items = relationship("ArticleDb", back_populates="user")
    
class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    author = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
    published = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="articles")
    
from typing import List
from database.schema import ArticleBase, Article
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.config import get_db
from database import article_db

router = APIRouter(
    prefix='/article',
    tags=['article_get']
)

# get all articles

@router.get('/', response_model=List[Article],
            summary="Get all articles",
            description="Get all articles from the database"
            )

def get_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    articles = article_db.get_articles(db, skip, limit)
    return articles

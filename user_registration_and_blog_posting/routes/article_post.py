from typing import List
from database.schema import ArticleBase, Article
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.config import get_db
from database import article_db

router = APIRouter(
    prefix='/article',
    tags=['article_post']
)

# create article

@router.post('/', response_model=Article,
             summary="Create an article",
             description="Create an article in the database"
             )

def create_article(request: ArticleBase, db: Session = Depends(get_db),):
    return article_db.create_article(db, request)


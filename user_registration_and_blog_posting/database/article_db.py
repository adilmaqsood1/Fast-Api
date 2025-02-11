from sqlalchemy.orm import Session
from database.models import Article
from database.schema import ArticleBase

def create_article(db: Session, article: ArticleBase):
    new_article = Article(title=article.title, content=article.content)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

def get_articles(db: Session, skip: int = 0, limit: int = 10):
    article = db.query(Article).filter(Article.published == True).offset(skip).limit(limit).all()
    return article
from fastapi import FastAPI, HTTPException, Depends, status, Query
from pydantic import BaseModel, Field
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from logging import logger
from typing import List

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Book(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)


BOOKS = []


@app.get("/",
         tags= ["Books"],
         summary="Read all books",
         description="every book which is in database is gonna show over here",
         status_code=status.HTTP_200_OK)

def read_api(db: Session = Depends(get_db),
             read_books: str = Query(None, title="Read all books")) -> List[models.Books]:
    logger.info("Reading all books")
    return db.query(models.Books).all()


@app.post("/",
          tags= ["create_book"],
          summary="Create a book",
          description="Create a book with title, author, description and rating",
          status_code=status.HTTP_201_CREATED
          )

def create_book(book: Book, db: Session = Depends(get_db),
                create_book: str = Query(None, title="Create a book"),
                create_author: str = Query(None, title="Create a author"),
                create_description: str = Query(None, title="Create a description"),
                create_rating: int = Query(None, title="Create a rating")
):
    logger.info(f"Creating book: {book.title}")
    book_model = models.Books()
    book_model.title = book.title
    book_model.author = book.author
    book_model.description = book.description
    book_model.rating = book.rating

    db.add(book_model)
    db.commit()

    return book


@app.put("/{book_id}",
         tags= ["update_book"],
         summary="Update a book",
         description="Update a book with title, author, description and rating",
         status_code=status.HTTP_200_OK
         )
def update_book(book_id: int, book: Book, db: Session = Depends(get_db),
                update_book: str = Query(None, title="Update a book"),
                update_author: str = Query(None, title="Update a author"),
                update_description: str = Query(None, title="Update a description"),
                update_rating: int = Query(None, title="Update a rating")
                ):

    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()

    if book_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {book_id} : Does not exist"
        )

    book_model.title = book.title
    book_model.author = book.author
    book_model.description = book.description
    book_model.rating = book.rating

    db.add(book_model)
    db.commit()

    return book


@app.delete("/{book_id}",
            tags= ["delete_book"],
            summary="Delete a book",
            description="Delete a book with title, author, description and rating",
            status_code=status.HTTP_200_OK
            )
def delete_book(book_id: int, db: Session = Depends(get_db),
                delete_book: str = Query(None, title="Delete a book")
                ):

    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()

    if book_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {book_id} : Does not exist"
        )

    db.query(models.Books).filter(models.Books.id == book_id).delete()

    db.commit()

from fastapi import FastAPI
from routes import route_get, route_post, user, article_get, article_post
from database.config import engine
from database import models

app = FastAPI()

@app.get('/')
def index():
  return {'message': 'Hello world!'}


app.include_router(user.router)
app.include_router(route_get.router)
app.include_router(route_post.router)
app.include_router(article_get.router)
app.include_router(article_post.router)


models.Base.metadata.create_all(engine)
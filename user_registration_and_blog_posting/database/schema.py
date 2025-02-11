from pydantic import BaseModel


class Article(BaseModel):
    title: str
    content: str
    author_id: int
    created_at: str
    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    id: int
    username: str
    email: str
    items: list[Article] = []
    class Config:
        from_attributes = True 

class User(UserBase):
    id: int
    class Config:
        orm_mode = True
        
class ArticleBase(BaseModel):
    title: str
    content: str
    created_id: int
    published: str
    user: User
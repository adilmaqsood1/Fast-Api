from fastapi import APIRouter

router = APIRouter(
    prefix='/blog',
    tags=['blog_post']
)

@router.post('/new')
def create_blog():
  pass
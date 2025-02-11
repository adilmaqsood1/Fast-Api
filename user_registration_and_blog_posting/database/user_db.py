from database.hash import Hash
from sqlalchemy.orm.session import Session
from database.schema import UserBase
from database.models import User


def create_user(db: Session, request: UserBase):
  new_user = User(
    username = request.username,
    email = request.email,
    password = Hash.bcrypt(request.password)
  )
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

from ..uow import UnitOfWork
from ..models import User
from ..database import session_maker
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
    return pwd_context.hash(password)

def authenticate_user(username: str, password: str):
    with UnitOfWork(session_factory=session_maker) as uow:
      user = uow.users.get_by_username(username)
      if not user:
          return False
      if not verify_password(password, user.hashed_password):
          return False
      return user
    
def get_user_by_username(username: str): 
    with UnitOfWork(session_factory=session_maker) as uow:
      uow.users.get_by_username(username)

def create_user(user: User): 
    with UnitOfWork(session_factory=session_maker) as uow:
      uow.users.add(user)
      
def update_user(id: str, user: User):
    with UnitOfWork(session_factory=session_maker) as uow:
      uow.users.update(id, user)
      
def get_users():
    with UnitOfWork(session_factory=session_maker) as uow:
      return uow.users.get_all()
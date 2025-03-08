from abc import ABC, abstractmethod
from sqlmodel import Session,select
from typing import Optional
from .base import GenericRepository, GenericSqlRepository
from ..models import User

class UserRepositoryBase(GenericRepository[User], ABC):
    @abstractmethod
    def get_by_name(self, name: str) -> Optional[User]:
        raise NotImplementedError()

    def get_by_username(self, name: str) -> Optional[User]:
        raise NotImplementedError()

class UserRepository(GenericSqlRepository[User], UserRepositoryBase):
    def __init__(self, session: Session) -> None:
        super().__init__(session, User)

    def get_by_name(self, name: str) -> Optional[User]:
        stmt = select(User).where(User.name == name)
        return self._session.exec(stmt).first()
      
    def get_by_username(self, username: str) -> Optional[User]:
        stmt = select(User).where(User.username == username)
        return self._session.exec(stmt).first()      
from abc import ABC, abstractmethod
from typing import TypeVar, Optional
from sqlmodel import Session, SQLModel, select
from .base import GenericRepository, GenericSqlRepository
from ..models import Manager

T = TypeVar("T", bound=SQLModel)

class ManagerRepositoryBase(GenericRepository[Manager], ABC):
    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Manager]:
        raise NotImplementedError()
      
class ManagerRepository(GenericSqlRepository[Manager], ManagerRepositoryBase):
    def __init__(self, session: Session) -> None:
        super().__init__(session, Manager)

    def get_by_name(self, name: str) -> Optional[Manager]:
        stmt = select(Manager).where(Manager.name == name)
        return self._session.exec(stmt).first()
from abc import ABC, abstractmethod
from typing import TypeVar, Optional
from sqlmodel import Session, SQLModel, select
from .base import GenericRepository, GenericSqlRepository
from ..models import Owner

T = TypeVar("T", bound=SQLModel)

class OwnerRepositoryBase(GenericRepository[Owner], ABC):
    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Owner]:
        raise NotImplementedError()
      
class OwnerRepository(GenericSqlRepository[Owner], OwnerRepositoryBase):
    def __init__(self, session: Session) -> None:
        super().__init__(session, Owner)

    def get_by_name(self, name: str) -> Optional[Owner]:
        stmt = select(Owner).where(Owner.name == name)
        return self._session.exec(stmt).first()
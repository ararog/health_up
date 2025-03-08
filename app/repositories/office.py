from abc import ABC, abstractmethod
from sqlmodel import Session,select
from typing import Optional
from .base import GenericRepository, GenericSqlRepository
from ..models import Office

class OfficeRepositoryBase(GenericRepository[Office], ABC):
    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Office]:
        raise NotImplementedError()

class OfficeRepository(GenericSqlRepository[Office], OfficeRepositoryBase):
    def __init__(self, session: Session) -> None:
        super().__init__(session, Office)

    def get_by_name(self, name: str) -> Optional[Office]:
        stmt = select(Office).where(Office.name == name)
        return self._session.exec(stmt).first()
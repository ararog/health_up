from abc import ABC, abstractmethod
from typing import TypeVar, Optional
from sqlmodel import Session, SQLModel, select
from .base import GenericRepository, GenericSqlRepository
from ..models import Doctor

T = TypeVar("T", bound=SQLModel)

class DoctorRepositoryBase(GenericRepository[Doctor], ABC):
    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Doctor]:
        raise NotImplementedError()
      
class DoctorRepository(GenericSqlRepository[Doctor], DoctorRepositoryBase):
    def __init__(self, session: Session) -> None:
        super().__init__(session, Doctor)

    def get_by_name(self, name: str) -> Optional[Doctor]:
        stmt = select(Doctor).where(Doctor.name == name)
        return self._session.exec(stmt).first()
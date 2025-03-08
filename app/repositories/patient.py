from abc import ABC, abstractmethod
from typing import TypeVar, Optional
from sqlmodel import Session, SQLModel, select
from .base import GenericRepository, GenericSqlRepository
from ..models import Patient

T = TypeVar("T", bound=SQLModel)

class PatientRepositoryBase(GenericRepository[Patient], ABC):
    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Patient]:
        raise NotImplementedError()
      
class PatientRepository(GenericSqlRepository[Patient], PatientRepositoryBase):
    def __init__(self, session: Session) -> None:
        super().__init__(session, Patient)

    def get_by_name(self, name: str) -> Optional[Patient]:
        stmt = select(Patient).where(Patient.name == name)
        return self._session.exec(stmt).first()
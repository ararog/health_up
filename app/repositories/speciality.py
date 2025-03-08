from abc import ABC, abstractmethod
from sqlmodel import Session,select
from typing import Optional
from .base import GenericRepository, GenericSqlRepository
from ..models import Speciality

class SpecialityRepositoryBase(GenericRepository[Speciality], ABC):
    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Speciality]:
        raise NotImplementedError()

class SpecialityRepository(GenericSqlRepository[Speciality], SpecialityRepositoryBase):
    def __init__(self, session: Session) -> None:
        super().__init__(session, Speciality)

    def get_by_name(self, name: str) -> Optional[Speciality]:
        stmt = select(Speciality).where(Speciality.name == name)
        return self._session.exec(stmt).first()
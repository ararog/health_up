from abc import ABC, abstractmethod
from sqlmodel import Session,select
from typing import Optional
from .base import GenericRepository, GenericSqlRepository
from ..models import Appointment

class AppointmentRepositoryBase(GenericRepository[Appointment], ABC):
    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Appointment]:
        raise NotImplementedError()


class AppointmentRepository(GenericSqlRepository[Appointment], AppointmentRepositoryBase):
    def __init__(self, session: Session) -> None:
        super().__init__(session, Appointment)

    def get_by_name(self, name: str) -> Optional[Appointment]:
        stmt = select(Appointment).where(Appointment.name == name)
        return self._session.exec(stmt).first()
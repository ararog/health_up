from ..uow import UnitOfWork
from ..models import Speciality
from ..database import session_maker

def create_speciality(speciality: Speciality): 
    with UnitOfWork(session_factory=session_maker) as uow:
      uow.specialities.add(speciality)
      
def update_speciality(id: str, speciality: Speciality):
    with UnitOfWork(session_factory=session_maker) as uow:
      uow.specialities.update(id, speciality)

def get_specialities():
    with UnitOfWork(session_factory=session_maker) as uow:
      return uow.specialities.get_all()
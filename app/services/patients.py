from ..uow import UnitOfWork
from ..models import Patient
from ..database import session_maker

def create_patient(patient: Patient): 
    with UnitOfWork(session_factory=session_maker) as uow:
      uow.patients.add(patient)

def update_patient(id: str, patient: Patient):
    with UnitOfWork(session_factory=session_maker) as uow:
      uow.patients.update(id, patient)
      
def get_patients():
    with UnitOfWork(session_factory=session_maker) as uow:
      return uow.patients.get_all()
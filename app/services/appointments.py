from ..uow import UnitOfWork
from ..models import Appointment
from ..database import session_maker

def create_appointment(appointment: Appointment): 
    with UnitOfWork(session_factory=session_maker) as uow:
        uow.appointments.add(appointment)
      
def update_appointment(id: str, appointment: Appointment):
    with UnitOfWork(session_factory=session_maker) as uow:
        uow.appointments.update(id, appointment)
      
def get_appointments():
    with UnitOfWork(session_factory=session_maker) as uow:
        return uow.appointments.get_all()
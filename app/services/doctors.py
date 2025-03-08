from ..uow import UnitOfWork
from ..models import Contact
from ..database import session_maker

def create_doctor(contact: Contact): 
    with UnitOfWork(session_factory=session_maker) as uow:
      uow.contacts.add(contact)
      
def update_doctor(id: str, contact: Contact):
    with UnitOfWork(session_factory=session_maker) as uow:
      uow.contacts.update(id, contact)

def get_doctors():
    with UnitOfWork(session_factory=session_maker) as uow:
      return uow.contacts.get_all()
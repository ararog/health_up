from ..uow import UnitOfWork
from ..models import Manager
from ..database import session_maker

def create_manager(contact: Manager): 
    with UnitOfWork(session_factory=session_maker) as uow:
      uow.managers.add(contact)
      
def update_manager(id: str, contact: Manager):
    with UnitOfWork(session_factory=session_maker) as uow:
      uow.managers.update(id, contact)

def get_managers():
    with UnitOfWork(session_factory=session_maker) as uow:
      return uow.managers.get_all()
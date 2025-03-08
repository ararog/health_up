from ..uow import UnitOfWork
from ..models import Owner
from ..database import session_maker

def create_owner(owner: Owner): 
    with UnitOfWork(session_factory=session_maker) as uow:
      uow.owners.add(owner)
      
def update_owner(id: str, owner: Owner):
    with UnitOfWork(session_factory=session_maker) as uow:
      uow.owners.update(id, owner)

def get_owners():
    with UnitOfWork(session_factory=session_maker) as uow:
      return uow.owners.get_all()
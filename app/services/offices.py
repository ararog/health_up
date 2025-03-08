from ..uow import UnitOfWork
from ..models import Office
from ..database import session_maker

def create_office(office: Office): 
    with UnitOfWork(session_factory=session_maker) as uow:
      uow.offices.add(office)
      
def update_office(id: str, office: Office):
    with UnitOfWork(session_factory=session_maker) as uow:
      uow.offices.update(id, office)

def get_offices():
    with UnitOfWork(session_factory=session_maker) as uow:
      return uow.offices.get_all()
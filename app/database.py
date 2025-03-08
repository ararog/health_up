from typing import Callable
from decouple import config
from sqlmodel import create_engine, Session, SQLModel

def sqlmodel_session_maker(engine) -> Callable[[], Session]:
    """Returns a SQLModel session maker function.

    Args:
        engine (_type_): SQLModel engine.

    Returns:
        Callable[[], Session]: Session maker function.
    """
    return lambda: Session(bind=engine, autocommit=False, autoflush=False)

database_url = config("DATABASE_URL")
  
engine = create_engine(database_url, echo=True)

session_maker = sqlmodel_session_maker(engine)


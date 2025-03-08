from abc import ABC, abstractmethod
from typing import Callable
from sqlmodel import Session

from .repositories.office import (
    OfficeRepositoryBase, 
    OfficeRepository
)

from .repositories.speciality import (
    SpecialityRepositoryBase,
    SpecialityRepository
)

from .repositories.doctor import (
    DoctorRepositoryBase,
    DoctorRepository
)

from .repositories.patient import (
    PatientRepositoryBase,
    PatientRepository
)

from .repositories.owner import (
    OwnerRepositoryBase,
    OwnerRepository
)

from .repositories.manager import (
    ManagerRepositoryBase,
    ManagerRepository
)

from .repositories.appointment import (
    AppointmentRepositoryBase, 
    AppointmentRepository
)


from .repositories.user import (
    UserRepositoryBase, 
    UserRepository
)

class UnitOfWorkBase(ABC):
    """Unit of work.
    """

    offices: OfficeRepositoryBase
    appointments: AppointmentRepositoryBase
    users: UserRepositoryBase
    doctors: DoctorRepositoryBase
    patients: PatientRepositoryBase
    managers: ManagerRepositoryBase
    owners: OwnerRepositoryBase
    specialities: SpecialityRepositoryBase

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.rollback()

    @abstractmethod
    def commit(self):
        """Commits the current transaction.
        """
        raise NotImplementedError()

    @abstractmethod
    def rollback(self):
        """Rollbacks the current transaction.
        """
        raise NotImplementedError()


class UnitOfWork(UnitOfWorkBase):
    def __init__(self, session_factory: Callable[[], Session]) -> None:
        """Creates a new uow instance.

        Args:
            session_factory (Callable[[], Session]): Session maker function.
        """
        self._session_factory = session_factory

    def __enter__(self):
        self._session = self._session_factory()
        self.offices = OfficeRepository(self._session)
        self.users = UserRepository(self._session)
        self.doctors = DoctorRepository(self._session)
        self.patients = PatientRepository(self._session)
        self.managers = ManagerRepository(self._session)
        self.owners = OwnerRepository(self._session)
        self.appointments = AppointmentRepository(self._session)
        self.specialities = SpecialityRepository(self._session)
        return super().__enter__()

    def commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()
from uuid_extensions import uuid7str
from app.uow import UnitOfWork
from app.database import session_maker
from app.models import (
  Office, 
  Doctor, 
  Speciality, 
  User,
  Manager,
  Owner
)

def main():
    with UnitOfWork(session_factory=session_maker) as uow:
        office = Office(
            id=uuid7str(),
            name="Health Up",
            description="Nós cuidamos de sua saúde dental!",
            phone_number="1234567890",
            address="123 Main St",
            website="www.healthup.com",
            email="info@healthup.com",
            opening_hours="9am-5pm, Monday-Friday",
            maps_link="https://maps.google.com/maps?q=123+Main+St,+Anytown,+USA",
            reviews="Great place to get your health needs met!",
        )
        uow.offices.add(office)
        
        speciality = Speciality(
            id=uuid7str(),
            name="Dentista",
            description="Especialista em implantes e cirurgia maxilofacial.",
            office_id=office.id,
        )
        uow.specialities.add(speciality)
        
        doctor = Doctor(
            id=uuid7str(),
            name="Dr. Sandro Araújo",
            phone_number="+5562982892988",
            bio="Dentista especialista em implantes e cirurgia maxilofacial.",
            office_id=office.id,
        )
        uow.doctors.add(doctor)

        manager = Manager(
            id=uuid7str(),
            name="Lidiana Silva",
            phone_number="+5562994493469",
            bio="Gerente do consultorio Health Up.",
            office_id=office.id,
        )
        uow.managers.add(manager)
        
        owner = Owner(
            id=uuid7str(),
            name="Riseli Araújo",
            phone_number="+5562981134209",
            bio="Dona do consultorio Health Up.",
            office_id=office.id,
        )
        uow.owners.add(owner)
        
        user = User(
            id=uuid7str(),
            name="Rogério Araújo",
            role="superadmin",
            email="rogerio@health-up.ai",
            username="rogerio",
            password="123456",
            office_id=office.id,
        )
        uow.users.add(user)
        
        uow.commit()
        
if __name__ == "__main__":
  main()
        
from uuid_extensions import uuid7str
from app.uow import UnitOfWork
from app.database import session_maker
from app.models import Office, Doctor, Speciality, User

def main():
    with UnitOfWork(session_factory=session_maker) as uow:
        office = Office(
            id=uuid7str(),
            name="Health Up",
            description="We provide top-notch healthcare services.",
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
            name="Cardiology",
            description="Specializing in heart health.",
            office_id=office.id,
        )
        uow.specialities.add(speciality)
        
        doctor = Doctor(
            id=uuid7str(),
            name="Dr. John Doe",
            description="Board-certified cardiologist.",
            office_id=office.id,
        )
        uow.doctors.add(doctor)
        
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
        
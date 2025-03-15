import random
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Captain, Airplane, Passenger
import ipdb

# Create an instance of Faker
fake = Faker()

# Database connection
engine = create_engine("sqlite:///air_travel.db")
Session = sessionmaker(bind=engine)
session = Session()

# Function to create an airplane
def create_airplane():
    airplane = Airplane(
        model=fake.word(),
        capacity=random.randint(50, 300),
        airline=fake.company(),  # Add a random company for the airline column
        manufacture_year=random.randint(1980, 2023)  # Add a manufacture year within a reasonable range
    )
    return airplane
# Function to create a captain
def create_captain():
    airplanes = session.query(Airplane.airplane_id).all()
    if not airplanes:  # Ensure airplanes exist in the database
        raise ValueError("No airplanes found. Please seed the Airplane table first.")
    
    captain = Captain(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        license_number=fake.unique.bothify(text='??-####-???'),
        airplane_id=random.choice(airplanes)[0]
    )
    return captain

# Function to create a passenger
def create_passenger():
    passenger = Passenger(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        passport_number=fake.unique.bothify(text='??#######'),
        email=fake.email()
    )
    return passenger

# Function to seed the database
def seed_database():
    # Seed airplanes
    airplanes = [create_airplane() for _ in range(5)]
    session.add_all(airplanes)
    session.commit()

    # Seed captains
    captains = [create_captain() for _ in range(10)]
    session.add_all(captains)
    session.commit()

    # Seed passengers
    passengers = [create_passenger() for _ in range(100)]
    session.add_all(passengers)
    session.commit()

# Main execution
if __name__ == "__main__":
    # Create tables in the database
    Base.metadata.create_all(engine)

    # Seed the database
    seed_database()

    # Debugging breakpoint
    ipdb.set_trace()

import ipdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Airplane, Flight, Passenger, Booking, Airport  # Make sure to import your models
from datetime import datetime

# Database URL - Change it to your own database URL
DATABASE_URL = "sqlite:///air_travel.db"  # Example for SQLite

# Create an engine and a session
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables
Base.metadata.create_all(engine)

# Seed data
def seed_data():
    # Create Airplanes
    airplane1 = Airplane(model="Boeing 737", capacity=150, airline="Airline A", manufacture_year=2015)
    airplane2 = Airplane(model="Airbus 320", capacity=180, airline="Airline B", manufacture_year=2018)

    # Create Airports
    airport1 = Airport(name="Airport A", location="City A", code="AAA", capacity=5000)
    airport2 = Airport(name="Airport B", location="City B", code="BBB", capacity=6000)

    # Add Airplanes and Airports to the session
    session.add(airplane1)
    session.add(airplane2)
    session.add(airport1)
    session.add(airport2)

    # Create Flights
    flight1 = Flight(flight_number="AA101", departure_time=datetime.strptime("2025-03-20 10:00:00", "%Y-%m-%d %H:%M:%S"), 
                     arrival_time=datetime.strptime("2025-03-20 12:00:00", "%Y-%m-%d %H:%M:%S"),
                     destination="City B", airplane=airplane1, airport=airport1)
    flight2 = Flight(flight_number="BB202", departure_time=datetime.strptime("2025-03-20 14:00:00", "%Y-%m-%d %H:%M:%S"),
                     arrival_time=datetime.strptime("2025-03-20 16:00:00", "%Y-%m-%d %H:%M:%S"),
                     destination="City A", airplane=airplane2, airport=airport2)

    # Add Flights to the session
    session.add(flight1)
    session.add(flight2)

    # Create Passengers
    passenger1 = Passenger(first_name="John", last_name="Doe", passport_number="X12345678", email="john.doe@example.com")
    passenger2 = Passenger(first_name="Jane", last_name="Smith", passport_number="Y98765432", email="jane.smith@example.com")

    # Add Passengers to the session
    session.add(passenger1)
    session.add(passenger2)

    # Create Bookings
    booking1 = Booking(seat_number="12A", booking_date=datetime.strptime("2025-03-10 15:00:00", "%Y-%m-%d %H:%M:%S"), flight=flight1, passenger=passenger1)
    booking2 = Booking(seat_number="15B", booking_date=datetime.strptime("2025-03-11 16:00:00", "%Y-%m-%d %H:%M:%S"), flight=flight2, passenger=passenger2)

    # Add Bookings to the session
    session.add(booking1)
    session.add(booking2)

    # Commit the session to save to the database
    session.commit()

# Enter the IPDB shell before committing if needed
ipdb.set_trace()

# Seed the data
seed_data()

# Close the session
session.close()

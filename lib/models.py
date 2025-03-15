from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import DateTime, ForeignKey, Column, Integer, String, Table
from datetime import datetime, timezone

Base = declarative_base()

# ASSOCIATION TABLE
PassengerFlightAssociation = Table(
    'passenger_flight_association', Base.metadata,
    Column('passenger_id', Integer, ForeignKey('passengers.passenger_id')),
    Column('flight_id', Integer, ForeignKey('flights.flight_id'))
)

class Captain(Base):
    __tablename__ = 'captains'
    captain_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name=Column(String, nullable=False)
    license_number=Column(String, nullable=False, unique=True)
    #A ONE TO ONE RELATIONSHIP
    #A Captain can only have its own airplane
    airplane_id = Column(Integer, ForeignKey('airplanes.airplane_id'))
    airplane = relationship('Airplane', back_populates='captains')


class Airplane(Base):
    __tablename__ = 'airplanes'
    airplane_id = Column(Integer, primary_key=True)
    model = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    airline = Column(String, nullable=False)
    manufacture_year = Column(Integer, nullable=False)
    #One to Many Relationship
    #An airplane can have several flights
    flights = relationship('Flight', back_populates='airplane')
    #One to one relationship
    captains = relationship('Captain', back_populates='airplane')

class Flight(Base):
    __tablename__ = 'flights'
    flight_id = Column(Integer, primary_key=True)
    flight_number = Column(String, nullable=False)
    departure_time = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    arrival_time = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    destination = Column(String, nullable=False)
    airplane_id = Column(Integer, ForeignKey('airplanes.airplane_id'))
    airport_id = Column(Integer, ForeignKey('airports.airport_id'))
    #ONE TO MANY RELATIONSHIP
    #A flight can have several airplanes
    airplane = relationship("Airplane", back_populates='flights')
    #A flight can be done on many airports
    airport = relationship("Airport", back_populates='flights')
    #A flight can have many bookings
    bookings = relationship("Booking", back_populates="flight")
    #A flight can have several passengers
    passengers = relationship("Passenger", secondary=PassengerFlightAssociation, back_populates='flights')

class Passenger(Base):
    __tablename__ = 'passengers'
    passenger_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    passport_number = Column(String, nullable=False)
    email = Column(String, nullable=False)
    #A Passenger can do several bookings
    bookings = relationship("Booking", back_populates='passenger')
    #Many to Many relationship => Many Passengers can be in many flights
    flights = relationship('Flight', secondary=PassengerFlightAssociation, back_populates='passengers')

class Booking(Base):
    __tablename__ = 'bookings'
    booking_id = Column(Integer, primary_key=True)
    flight_id = Column(Integer, ForeignKey('flights.flight_id'))
    passenger_id = Column(Integer, ForeignKey('passengers.passenger_id'))
    seat_number = Column(String, nullable=False)
    booking_date = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    #ONE TO MANY RELATIONSHIP
    #A booking can have several flights
    flight = relationship('Flight', back_populates='bookings')
    #A Booking can have many passengers
    passenger = relationship('Passenger', back_populates='bookings')

class Airport(Base):
    __tablename__ = 'airports'
    airport_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    code = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    #ONE TO MANY RELATIONSHIP
    #An airport can portray many flights
    flights = relationship('Flight', back_populates="airport")

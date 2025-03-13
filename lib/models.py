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

class Airplane(Base):
    __tablename__ = 'airplanes'
    airplane_id = Column(Integer, primary_key=True)
    model = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    airline = Column(String, nullable=False)
    manufacture_year = Column(Integer, nullable=False)
    flights = relationship('Flight', back_populates='airplane')

class Flight(Base):
    __tablename__ = 'flights'
    flight_id = Column(Integer, primary_key=True)
    flight_number = Column(String, nullable=False)
    departure_time = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    arrival_time = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    destination = Column(String, nullable=False)
    airplane_id = Column(Integer, ForeignKey('airplanes.airplane_id'))
    airport_id = Column(Integer, ForeignKey('airports.airport_id'))
    airplane = relationship("Airplane", back_populates='flights')
    airport = relationship("Airport", back_populates='flights')
    bookings = relationship("Booking", back_populates="flight")
    passengers = relationship("Passenger", secondary=PassengerFlightAssociation, back_populates='flights')

class Passenger(Base):
    __tablename__ = 'passengers'
    passenger_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    passport_number = Column(String, nullable=False)
    email = Column(String, nullable=False)
    bookings = relationship("Booking", back_populates='passenger')
    flights = relationship('Flight', secondary=PassengerFlightAssociation, back_populates='passengers')

class Booking(Base):
    __tablename__ = 'bookings'
    booking_id = Column(Integer, primary_key=True)
    flight_id = Column(Integer, ForeignKey('flights.flight_id'))
    passenger_id = Column(Integer, ForeignKey('passengers.passenger_id'))
    seat_number = Column(String, nullable=False)
    booking_date = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    flight = relationship('Flight', back_populates='bookings')
    passenger = relationship('Passenger', back_populates='bookings')

class Airport(Base):
    __tablename__ = 'airports'
    airport_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    code = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    flights = relationship('Flight', back_populates="airport")

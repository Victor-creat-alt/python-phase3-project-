from models import Airplane, Flight, Passenger, Booking, Airport
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

#DATABASE URL
DATABASE_URL = "sqlite:///air_travel.db"

#Create an engine and a seesion
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

#CRUD OPERATIONS
# 1. Create (Insert)
def create_airplane(model, capacity, airline, manufacture_year):
    airplane = Airplane(model=model, capacity=capacity, airline=airline, manufacture_year=manufacture_year)
    session.add(airplane)
    session.commit()
    return airplane

def create_flight(flight_number, departure_time, arrival_time, destination, airplane_id, airport_id):
    flight = Flight(flight_number=flight_number, departure_time=departure_time, arrival_time=arrival_time, destination=destination, airplane_id=airplane_id, airport_id=airport_id)
    session.add(flight)
    session.commit()
    return flight

#2. Read(Select)
def get_all_flights():
    return session.query(Flight).all()

def get_passenger_by_id(passenger_id):
    return session.query(Passenger).filter(Passenger.passenger_id == passenger_id).first()

#3. Update(Modify)
def update_airplane_capacity(airplane_id, new_capacity):
    airplane = session.query(Airplane).filter(Airplane.airplane_id==airplane_id).first()
    if airplane:
        airplane.capacity = new_capacity
        session.commit()
        return airplane
    return None

#4. Delete(Remove)
def delete_booking(booking_id):
    booking = session.query(Booking).filter(Booking.booking_id == booking_id).first()
    if booking:
        session.delete(booking)
        session.commit()
        return True
    return False

if __name__ == "__main__":
    #Create new airplane
    new_airplane = create_airplane("Boeing 777", 250, "Airline C", 2020)
    print(f"Created new airplane: {new_airplane.model}, Capacity: {new_airplane.capacity}")

    #Get all flights
    flights = get_all_flights()
    for flight in flights:
         print(f"Flight: {flight.flight_number} - {flight.destination}")

    #Update airplane capacity
    update_airplane = update_airplane_capacity(new_airplane.airplane_id, 300)
    print(f"Updated airplane capacity: {update_airplane.capacity}")    

    #Delete a booking
    deleted = delete_booking(1)
    print(f"Booking deleted: {deleted}")

    #Close session
    session.close()

print("No error in models.py")





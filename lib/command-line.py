from sqlalchemy import create_engine
from models import Base, Flight, Airport, Booking, Passenger, Airplane
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///air_travel.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def main_menu():
    while True:
        print("Welcome To The Air Travel Management System.")
        print("1. Manage Flights")
        print("2. Manage Passengers")
        print("3. Manage Bookings")
        print("4. Manage Airplanes")
        print("5. Manage Airports")
        print("6. Exit")
        option = input("Enter option:")
        if option == '1':
            flights_menu()
        elif option == '2':
            passengers_menu()
        elif option == '3':
            bookings_menu()
        elif option == '4':
            airplanes_menu()
        elif option == '5':
            airports_menu()
        elif option == '6':
            break
        else:
            print('Invalid choice. Please try again.')

def flights_menu():
    while True:
        print("\nFlights Menu")
        print("1. Create Flight")
        print("2. Delete Flight")
        print("3. Display All Flights")
        print("4. Find Flight by ID")
        print("5. Return to Main Menu")
        choice = input("Enter a choice:")
        if choice == '1':
            create_flight()
        elif choice == '2':
            delete_flight()
        elif choice == '3':
            display_all_flights()
        elif choice == '4':
            find_flight_by_id()
        elif choice == '5':
            break
        else:
            print('Invalid choice. Please try again.')

def create_flight():
    flight_number = input("Enter flight number:")
    departure_time_str = input("Enter departure time (YYYY-MM-DD HH:MM):")
    arrival_time_str = input("Enter arrival time (YYYY-MM-DD HH:MM):")
    
    # Convert the input string to a datetime object
    departure_time = datetime.strptime(departure_time_str, "%Y-%m-%d %H:%M")
    arrival_time = datetime.strptime(arrival_time_str, "%Y-%m-%d %H:%M")

    destination = input("Enter destination:")
    airplane_id = input("Enter airplane ID:")

    # Create the flight object
    flight = Flight(flight_number=flight_number, departure_time=departure_time, arrival_time=arrival_time, destination=destination, airplane_id=airplane_id)
    
    # Add flight to the session and commit
    session.add(flight)
    session.commit()
    print("The flight has been created successfully.")

def delete_flight():
    flight_id = input("Enter Flight ID to delete:")
    flight = session.query(Flight).get(flight_id)
    if flight:
        session.delete(flight)
        session.commit()
        print("Flight deleted.")
    else:
        print("The flight has not been found.")

def display_all_flights():
    flights = session.query(Flight).all()
    for flight in flights:
        print(f"ID: {flight.flight_id}, Number: {flight.flight_number}, Destination: {flight.destination}")

def find_flight_by_id():
    flight_id = input("Enter Flight ID to find:")
    flight = session.query(Flight).get(flight_id)
    if flight:
        print(f"ID: {flight.flight_id}, Number: {flight.flight_number}, Destination: {flight.destination}")
    else:
        print("The flight is unavailable.")

def passengers_menu():
    while True:
        print("\nPassengers Menu")
        print("1. Display All Passengers")
        print("2. Find Passenger by ID")
        print("3. Return to Main Menu")
        choice = input("Enter a choice:")
        if choice == '1':
            display_all_passengers()
        elif choice == '2':
            find_passenger_by_id()
        elif choice == '3':
            break
        else:
            print('Invalid choice. Please try again.')


def display_all_passengers():
    passengers = session.query(Passenger).all()
    for passenger in passengers:
        print(f"ID: {passenger.passenger_id}, Name: {passenger.name}, Passport Number: {passenger.passport_number}")

def find_passenger_by_id():
    passenger_id = input("Enter Passenger ID to find:")
    passenger = session.query(Passenger).get(passenger_id)
    if passenger:
        print(f"ID: {passenger.passenger_id}, Name: {passenger.name}, Passport Number: {passenger.passport_number}")
    else:
        print("The passenger is unavailable.")

def bookings_menu():
    while True:
        print("\nBookings Menu")
        print("1. Create Booking")
        print("2. Delete Booking")
        print("3. Display All Bookings")
        print("4. Find Booking by ID")
        print("5. Return to Main Menu")
        choice = input("Enter a choice:")
        if choice == '1':
            create_booking()
        elif choice == '2':
            delete_booking()
        elif choice == '3':
            display_all_bookings()
        elif choice == '4':
            find_booking_by_id()
        elif choice == '5':
            break
        else:
            print('Invalid choice. Please try again.')

def create_booking():
    passenger_id = input("Enter passenger ID:")
    flight_id = input("Enter flight ID:")
    booking = Booking(passenger_id=passenger_id, flight_id=flight_id)
    session.add(booking)
    session.commit()
    print("The booking has been created successfully.")

def delete_booking():
    booking_id = input("Enter Booking ID to delete:")
    booking = session.query(Booking).get(booking_id)
    if booking:
        session.delete(booking)
        session.commit()
        print("Booking deleted.")
    else:
        print("The booking has not been found.")

def display_all_bookings():
    bookings = session.query(Booking).all()
    for booking in bookings:
        print(f"ID: {booking.booking_id}, Passenger ID: {booking.passenger_id}, Flight ID: {booking.flight_id}")

def find_booking_by_id():
    booking_id = input("Enter Booking ID to find:")
    booking = session.query(Booking).get(booking_id)
    if booking:
        print(f"ID: {booking.booking_id}, Passenger ID: {booking.passenger_id}, Flight ID: {booking.flight_id}")
    else:
        print("The booking is unavailable.")

def airplanes_menu():
    while True:
        print("\nAirplanes Menu")
        print("1. Create Airplane")
        print("2. Delete Airplane")
        print("3. Display All Airplanes")
        print("4. Find Airplane by ID")
        print("5. Return to Main Menu")
        choice = input("Enter a choice:")
        if choice == '1':
            create_airplane()
        elif choice == '2':
            delete_airplane()
        elif choice == '3':
            display_all_airplanes()
        elif choice == '4':
            find_airplane_by_id()
        elif choice == '5':
            break
        else:
            print('Invalid choice. Please try again.')

def create_airplane():
    model = input("Enter airplane model:")
    capacity = input("Enter airplane capacity:")
    airplane = Airplane(model=model, capacity=capacity)
    session.add(airplane)
    session.commit()
    print("The airplane has been created successfully.")

def delete_airplane():
    airplane_id = input("Enter Airplane ID to delete:")
    airplane = session.query(Airplane).get(airplane_id)
    if airplane:
        session.delete(airplane)
        session.commit()
        print("Airplane deleted.")
    else:
        print("The airplane has not been found.")

def display_all_airplanes():
    airplanes = session.query(Airplane).all()
    for airplane in airplanes:
        print(f"ID: {airplane.airplane_id}, Model: {airplane.model}, Capacity: {airplane.capacity}")

def find_airplane_by_id():
    airplane_id = input("Enter Airplane ID to find:")
    airplane = session.query(Airplane).get(airplane_id)
    if airplane:
        print(f"ID: {airplane.airplane_id}, Model: {airplane.model}, Capacity: {airplane.capacity}")
    else:
        print("The airplane is unavailable.")

def airports_menu():
    while True:
        print("\nAirports Menu")
        print("1. Create Airport")
        print("2. Delete Airport")
        print("3. Display All Airports")
        print("4. Find Airport by ID")
        print("5. Return to Main Menu")
        choice = input("Enter a choice:")
        if choice == '1':
            create_airport()
        elif choice == '2':
            delete_airport()
        elif choice == '3':
            display_all_airports()
        elif choice == '4':
            find_airport_by_id()
        elif choice == '5':
            break
        else:
            print('Invalid choice. Please try again.')

def create_airport():
    name = input("Enter airport name:")
    location = input("Enter airport location:")
    airport = Airport(name=name, location=location)
    session.add(airport)
    session.commit()
    print("The airport has been created successfully.")

def delete_airport():
    airport_id = input("Enter Airport ID to delete:")
    airport = session.query(Airport).get(airport_id)
    if airport:
        session.delete(airport)
        session.commit()
        print("Airport deleted.")
    else:
        print("The airport has not been found.")

def display_all_airports():
    airports = session.query(Airport).all()
    for airport in airports:
        print(f"ID: {airport.airport_id}, Name: {airport.name}, Location: {airport.location}")

def find_airport_by_id():
    airport_id = input("Enter Airport ID to find:")
    airport = session.query(Airport).get(airport_id)
    if airport:
        print(f"ID: {airport.airport_id}, Name: {airport.name}, Location: {airport.location}")
    else:
        print("The airport is unavailable.")

if __name__ == '__main__':
    main_menu()





print("No error in commandline.py")

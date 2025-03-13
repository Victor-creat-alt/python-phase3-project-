from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Airplane, Flight, Passenger, Booking, Airport, MaintenanceRecord
from datetime import datetime

# Setting up the database connection and session
engine = create_engine('sqlite:///air_travel.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Main Menu
def main_menu():
    while True:
        print("Welcome To The Air Travel Management System.")
        print("1. Manage Flights")
        print("2. Manage Passengers")
        print("3. Manage Bookings")
        print("4. Manage Airplanes")
        print("5. Manage Airports")
        print("6. Manage Maintenance Records")
        print("7. Exit")
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
            maintenance_records_menu()
        elif option == '7':
            break
        else:
            print('Invalid choice. Please try again.')

# Flights Menu
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

# Create Flight
def create_flight():
    flight_number = input("Enter flight number:")
    departure_time_str = input("Enter departure time (YYYY-MM-DD HH:MM):")
    arrival_time_str = input("Enter arrival time (YYYY-MM-DD HH:MM):")
    
    # Convert the input string to a datetime object
    departure_time = datetime.strptime(departure_time_str, "%Y-%m-%d %H:%M")
    arrival_time = datetime.strptime(arrival_time_str, "%Y-%m-%d %H:%M")

    destination = input("Enter destination:")
    airplane_id = input("Enter airplane ID:")
    airport_id = input("Enter airport ID:")

    # Create the flight object
    flight = Flight(flight_number=flight_number, departure_time=departure_time, arrival_time=arrival_time, destination=destination, airplane_id=airplane_id, airport_id=airport_id)
    
    # Add flight to the session and commit
    session.add(flight)
    session.commit()
    print("The flight has been created successfully.")

# Delete Flight
def delete_flight():
    flight_id = input("Enter Flight ID to delete:")
    flight = session.query(Flight).get(flight_id)
    if flight:
        session.delete(flight)
        session.commit()
        print("Flight deleted.")
    else:
        print("The flight has not been found.")

# Display All Flights
def display_all_flights():
    flights = session.query(Flight).all()
    for flight in flights:
        print(f"ID: {flight.flight_id}, Number: {flight.flight_number}, Destination: {flight.destination}")

# Find Flight by ID
def find_flight_by_id():
    flight_id = input("Enter Flight ID to find:")
    flight = session.query(Flight).get(flight_id)
    if flight:
        print(f"ID: {flight.flight_id}, Number: {flight.flight_number}, Destination: {flight.destination}")
    else:
        print("The flight is unavailable.")

# Passengers Menu
def passengers_menu():
    while True:
        print("\nPassengers Menu")
        print("1. Create Passenger")
        print("2. Display All Passengers")
        print("3. Find Passenger by ID")
        print("4. Return to Main Menu")
        choice = input("Enter a choice:")
        if choice == '1':
            create_passenger()
        elif choice == '2':
            display_all_passengers()
        elif choice == '3':
            find_passenger_by_id()
        elif choice == '4':
            break
        else:
            print('Invalid choice. Please try again.')

# Create Passenger
def create_passenger():
    first_name = input("Enter first name:")
    last_name = input("Enter last name:")
    passport_number = input("Enter passport number:")
    email = input("Enter email:")

    passenger = Passenger(first_name=first_name, last_name=last_name, passport_number=passport_number, email=email)
    
    session.add(passenger)
    session.commit()
    print("The passenger has been created successfully.")

# Display All Passengers
def display_all_passengers():
    passengers = session.query(Passenger).all()
    for passenger in passengers:
        print(f"ID: {passenger.passenger_id}, Name: {passenger.first_name} {passenger.last_name}, Passport: {passenger.passport_number}")

# Find Passenger by ID
def find_passenger_by_id():
    passenger_id = input("Enter Passenger ID to find:")
    passenger = session.query(Passenger).get(passenger_id)
    if passenger:
        print(f"ID: {passenger.passenger_id}, Name: {passenger.first_name} {passenger.last_name}, Passport: {passenger.passport_number}")
    else:
        print("The passenger is unavailable.")

# Bookings Menu
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

# Create Booking
def create_booking():
    passenger_id = input("Enter passenger ID:")
    flight_id = input("Enter flight ID:")
    seat_number = input("Enter seat number:")
    
    booking = Booking(passenger_id=passenger_id, flight_id=flight_id, seat_number=seat_number)
    session.add(booking)
    session.commit()
    print("The booking has been created successfully.")

# Delete Booking
def delete_booking():
    booking_id = input("Enter Booking ID to delete:")
    booking = session.query(Booking).get(booking_id)
    if booking:
        session.delete(booking)
        session.commit()
        print("Booking deleted.")
    else:
        print("The booking has not been found.")

# Display All Bookings
def display_all_bookings():
    bookings = session.query(Booking).all()
    for booking in bookings:
        print(f"ID: {booking.booking_id}, Passenger ID: {booking.passenger_id}, Flight ID: {booking.flight_id}, Seat: {booking.seat_number}")

# Find Booking by ID
def find_booking_by_id():
    booking_id = input("Enter Booking ID to find:")
    booking = session.query(Booking).get(booking_id)
    if booking:
        print(f"ID: {booking.booking_id}, Passenger ID: {booking.passenger_id}, Flight ID: {booking.flight_id}, Seat: {booking.seat_number}")
    else:
        print("The booking is unavailable.")

# Airplanes Menu
def airplanes_menu():
    while True:
        print("\nAirplanes Menu")
        print("1. Create Airplane")
        print("2. Display All Airplanes")
        print("3. Find Airplane by ID")
        print("4. Return to Main Menu")
        choice = input("Enter a choice:")
        if choice == '1':
            create_airplane()
        elif choice == '2':
            display_all_airplanes()
        elif choice == '3':
            find_airplane_by_id()
        elif choice == '4':
            break
        else:
            print('Invalid choice. Please try again.')

# Create Airplane
def create_airplane():
    model = input("Enter airplane model:")
    capacity = input("Enter airplane capacity:")
    airline = input("Enter airline name:")
    manufacture_year = input("Enter manufacture year:")

    airplane = Airplane(model=model, capacity=capacity, airline=airline, manufacture_year=manufacture_year)
    
    session.add(airplane)
    session.commit()
    print("The airplane has been created successfully.")

# Display All Airplanes
def display_all_airplanes():
    airplanes = session.query(Airplane).all()
    for airplane in airplanes:
        print(f"ID: {airplane.airplane_id}, Model: {airplane.model}, Airline: {airplane.airline}, Capacity: {airplane.capacity}")

# Find Airplane by ID
def find_airplane_by_id():
    airplane_id = input("Enter Airplane ID to find:")
    airplane = session.query(Airplane).get(airplane_id)
    if airplane:
        print(f"ID: {airplane.airplane_id}, Model: {airplane.model}, Airline: {airplane.airline}, Capacity: {airplane.capacity}")
    else:
        print("The airplane is unavailable.")

# Airports Menu
def airports_menu():
    while True:
        print("\nAirports Menu")
        print("1. Create Airport")
        print("2. Display All Airports")
        print("3. Find Airport by ID")
        print("4. Return to Main Menu")
        choice = input("Enter a choice:")
        if choice == '1':
            create_airport()
        elif choice == '2':
            display_all_airports()
        elif choice == '3':
            find_airport_by_id()
        elif choice == '4':
            break
        else:
            print('Invalid choice. Please try again.')

# Create Airport
def create_airport():
    name = input("Enter airport name:")
    location = input("Enter airport location:")
    code = input("Enter airport code:")
    capacity = input("Enter airport capacity:")

    airport = Airport(name=name, location=location, code=code, capacity=capacity)
    
    session.add(airport)
    session.commit()
    print("The airport has been created successfully.")

# Display All Airports
def display_all_airports():
    airports = session.query(Airport).all()
    for airport in airports:
        print(f"ID: {airport.airport_id}, Name: {airport.name}, Location: {airport.location}")

# Find Airport by ID
def find_airport_by_id():
    airport_id = input("Enter Airport ID to find:")
    airport = session.query(Airport).get(airport_id)
    if airport:
        print(f"ID: {airport.airport_id}, Name: {airport.name}, Location: {airport.location}")
    else:
        print("The airport is unavailable.")

# Maintenance Records Menu
def maintenance_records_menu():
    while True:
        print("\nMaintenance Records Menu")
        print("1. Create Maintenance Record")
        print("2. Display All Maintenance Records")
        print("3. Find Maintenance Record by Airplane ID")
        print("4. Return to Main Menu")
        choice = input("Enter a choice:")
        if choice == '1':
            create_maintenance_record()
        elif choice == '2':
            display_all_maintenance_records()
        elif choice == '3':
            find_maintenance_record_by_airplane_id()
        elif choice == '4':
            break
        else:
            print('Invalid choice. Please try again.')

# Create Maintenance Record
def create_maintenance_record():
    airplane_id = input("Enter airplane ID:")
    last_maintenance_date = datetime.now()
    next_due_maintenance_date = input("Enter next due maintenance date (YYYY-MM-DD HH:MM):")
    next_due_maintenance_date = datetime.strptime(next_due_maintenance_date, "%Y-%m-%d %H:%M")

    maintenance_record = MaintenanceRecord(
        airplane_id=airplane_id,
        last_maintenance_date=last_maintenance_date,
        next_due_maintenance_date=next_due_maintenance_date
    )
    
    session.add(maintenance_record)
    session.commit()
    print("The maintenance record has been created successfully.")

# Display All Maintenance Records
def display_all_maintenance_records():
    maintenance_records = session.query(MaintenanceRecord).all()
    for record in maintenance_records:
        print(f"ID: {record.maintenance_id}, Airplane ID: {record.airplane_id}, Last Maintenance Date: {record.last_maintenance_date}, Next Due: {record.next_due_maintenance_date}")

# Find Maintenance Record by Airplane ID
def find_maintenance_record_by_airplane_id():
    airplane_id = input("Enter Airplane ID to find maintenance record:")
    record = session.query(MaintenanceRecord).filter_by(airplane_id=airplane_id).first()
    if record:
        print(f"ID: {record.maintenance_id}, Airplane ID: {record.airplane_id}, Last Maintenance Date: {record.last_maintenance_date}, Next Due: {record.next_due_maintenance_date}")
    else:
        print("Maintenance record not found.")

if __name__ == '__main__':
    main_menu()

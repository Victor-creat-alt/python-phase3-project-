import tkinter as tk
from tkinter import messagebox
from tkinter import font
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Flight, Passenger, Booking, Airplane, Airport

# Create engine and session
engine = create_engine('sqlite:///air_travel.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Function to create a Flight GUI with added styling
def create_flight_gui():
    def submit():
        flight_number = flight_number_entry.get()
        departure_time = departure_time_entry.get()
        arrival_time = arrival_time_entry.get()
        destination = destination_entry.get()
        airplane_id = airplane_id_entry.get()

        flight = Flight(
            flight_number=flight_number,
            departure_time=departure_time,
            arrival_time=arrival_time,
            destination=destination,
            airplane_id=airplane_id
        )

        session.add(flight)
        session.commit()
        messagebox.showinfo("Success", "The Flight has been created successfully")

    flight_gui = tk.Tk()
    flight_gui.title("Create Flight")
    flight_gui.config(bg="#f4f4f4")  # Light gray background

    # Set custom fonts
    header_font = font.Font(family="Helvetica", size=12, weight="bold")
    entry_font = font.Font(family="Arial", size=10)

    tk.Label(flight_gui, text="Flight Number", font=header_font, bg="#f4f4f4").grid(row=0, sticky="e", padx=10, pady=5)
    tk.Label(flight_gui, text="Departure Time (YYYY-MM-DD HH:MM)", font=header_font, bg="#f4f4f4").grid(row=1, sticky="e", padx=10, pady=5)
    tk.Label(flight_gui, text="Arrival Time (YYYY-MM-DD HH:MM)", font=header_font, bg="#f4f4f4").grid(row=2, sticky="e", padx=10, pady=5)
    tk.Label(flight_gui, text="Destination", font=header_font, bg="#f4f4f4").grid(row=3, sticky="e", padx=10, pady=5)
    tk.Label(flight_gui, text="Airplane ID", font=header_font, bg="#f4f4f4").grid(row=4, sticky="e", padx=10, pady=5)

    flight_number_entry = tk.Entry(flight_gui, font=entry_font)
    departure_time_entry = tk.Entry(flight_gui, font=entry_font)
    arrival_time_entry = tk.Entry(flight_gui, font=entry_font)
    destination_entry = tk.Entry(flight_gui, font=entry_font)
    airplane_id_entry = tk.Entry(flight_gui, font=entry_font)

    flight_number_entry.grid(row=0, column=1, padx=10, pady=5)
    departure_time_entry.grid(row=1, column=1, padx=10, pady=5)
    arrival_time_entry.grid(row=2, column=1, padx=10, pady=5)
    destination_entry.grid(row=3, column=1, padx=10, pady=5)
    airplane_id_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Button(flight_gui, text="Submit", command=submit, bg="#4CAF50", fg="white", font=header_font).grid(row=5, columnspan=2, pady=15)

    flight_gui.mainloop()

# Function to create a Passenger GUI with added styling
def create_passenger_gui():
    def submit():
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        passport_number = passport_number_entry.get()
        email = email_entry.get()

        passenger = Passenger(
            first_name=first_name,
            last_name=last_name,
            passport_number=passport_number,
            email=email
        )

        session.add(passenger)
        session.commit()
        messagebox.showinfo("Success", "The passenger has been added successfully")

    passenger_gui = tk.Tk()
    passenger_gui.title("Create Passenger")
    passenger_gui.config(bg="#f4f4f4")

    header_font = font.Font(family="Helvetica", size=12, weight="bold")
    entry_font = font.Font(family="Arial", size=10)

    tk.Label(passenger_gui, text="First Name", font=header_font, bg="#f4f4f4").grid(row=0, sticky="e", padx=10, pady=5)
    tk.Label(passenger_gui, text="Last Name", font=header_font, bg="#f4f4f4").grid(row=1, sticky="e", padx=10, pady=5)
    tk.Label(passenger_gui, text="Passport Number", font=header_font, bg="#f4f4f4").grid(row=2, sticky="e", padx=10, pady=5)
    tk.Label(passenger_gui, text="Email", font=header_font, bg="#f4f4f4").grid(row=3, sticky="e", padx=10, pady=5)

    first_name_entry = tk.Entry(passenger_gui, font=entry_font)
    last_name_entry = tk.Entry(passenger_gui, font=entry_font)
    passport_number_entry = tk.Entry(passenger_gui, font=entry_font)
    email_entry = tk.Entry(passenger_gui, font=entry_font)

    first_name_entry.grid(row=0, column=1, padx=10, pady=5)
    last_name_entry.grid(row=1, column=1, padx=10, pady=5)
    passport_number_entry.grid(row=2, column=1, padx=10, pady=5)
    email_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Button(passenger_gui, text="Submit", command=submit, bg="#4CAF50", fg="white", font=header_font).grid(row=4, columnspan=2, pady=15)

    passenger_gui.mainloop()

# Function to create Booking GUI with added styling
def create_booking_gui():
    def submit():
        flight_id = flight_id_entry.get()
        passenger_id = passenger_id_entry.get()
        seat_number = seat_number_entry.get()
        booking_date = booking_date_entry.get()

        booking = Booking(
            flight_id=flight_id,
            passenger_id=passenger_id,
            seat_number=seat_number,
            booking_date=booking_date
        )

        session.add(booking)
        session.commit()
        messagebox.showinfo("Success", "The booking has been done successfully")

    booking_gui = tk.Tk()
    booking_gui.title("Create Booking")
    booking_gui.config(bg="#f4f4f4")

    header_font = font.Font(family="Helvetica", size=12, weight="bold")
    entry_font = font.Font(family="Arial", size=10)

    tk.Label(booking_gui, text="Flight ID", font=header_font, bg="#f4f4f4").grid(row=0, sticky="e", padx=10, pady=5)
    tk.Label(booking_gui, text="Passenger ID", font=header_font, bg="#f4f4f4").grid(row=1, sticky="e", padx=10, pady=5)
    tk.Label(booking_gui, text="Seat Number", font=header_font, bg="#f4f4f4").grid(row=2, sticky="e", padx=10, pady=5)
    tk.Label(booking_gui, text="Booking Date (YYYY-MM-DD HH:MM)", font=header_font, bg="#f4f4f4").grid(row=3, sticky="e", padx=10, pady=5)

    flight_id_entry = tk.Entry(booking_gui, font=entry_font)
    passenger_id_entry = tk.Entry(booking_gui, font=entry_font)
    seat_number_entry = tk.Entry(booking_gui, font=entry_font)
    booking_date_entry = tk.Entry(booking_gui, font=entry_font)

    flight_id_entry.grid(row=0, column=1, padx=10, pady=5)
    passenger_id_entry.grid(row=1, column=1, padx=10, pady=5)
    seat_number_entry.grid(row=2, column=1, padx=10, pady=5)
    booking_date_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Button(booking_gui, text="Submit", command=submit, bg="#4CAF50", fg="white", font=header_font).grid(row=4, columnspan=2, pady=15)

    booking_gui.mainloop()

# Function to create Airplane GUI with added styling
def create_airplane_gui():
    def submit():
        model = model_entry.get()
        capacity = capacity_entry.get()
        airline = airline_entry.get()
        manufacture_year = manufacture_year_entry.get()

        airplane = Airplane(
            model=model,
            capacity=capacity,
            airline=airline,
            manufacture_year=manufacture_year
        )

        session.add(airplane)
        session.commit()
        messagebox.showinfo("Success", "The Airplane has been created successfully")

    airplane_gui = tk.Tk()
    airplane_gui.title("Create Airplane")
    airplane_gui.config(bg="#f4f4f4")

    header_font = font.Font(family="Helvetica", size=12, weight="bold")
    entry_font = font.Font(family="Arial", size=10)

    tk.Label(airplane_gui, text="Model", font=header_font, bg="#f4f4f4").grid(row=0, sticky="e", padx=10, pady=5)
    tk.Label(airplane_gui, text="Capacity", font=header_font, bg="#f4f4f4").grid(row=1, sticky="e", padx=10, pady=5)
    tk.Label(airplane_gui, text="Airline", font=header_font, bg="#f4f4f4").grid(row=2, sticky="e", padx=10, pady=5)
    tk.Label(airplane_gui, text="Manufacture Year", font=header_font, bg="#f4f4f4").grid(row=3, sticky="e", padx=10, pady=5)

    model_entry = tk.Entry(airplane_gui, font=entry_font)
    capacity_entry = tk.Entry(airplane_gui, font=entry_font)
    airline_entry = tk.Entry(airplane_gui, font=entry_font)
    manufacture_year_entry = tk.Entry(airplane_gui, font=entry_font)

    model_entry.grid(row=0, column=1, padx=10, pady=5)
    capacity_entry.grid(row=1, column=1, padx=10, pady=5)
    airline_entry.grid(row=2, column=1, padx=10, pady=5)
    manufacture_year_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Button(airplane_gui, text="Submit", command=submit, bg="#4CAF50", fg="white", font=header_font).grid(row=4, columnspan=2, pady=15)

    airplane_gui.mainloop()

# Function to create Airport GUI with added styling
def create_airport_gui():
    def submit():
        name = name_entry.get()
        location = location_entry.get()
        code = code_entry.get()
        capacity = capacity_entry.get()

        airport = Airport(
            name=name,
            location=location,
            code=code,
            capacity=capacity
        )

        session.add(airport)
        session.commit()
        messagebox.showinfo("Success", "The Airport has been created successfully")

    airport_gui = tk.Tk()
    airport_gui.title("Create Airport")
    airport_gui.config(bg="#f4f4f4")

    header_font = font.Font(family="Helvetica", size=12, weight="bold")
    entry_font = font.Font(family="Arial", size=10)

    tk.Label(airport_gui, text="Name", font=header_font, bg="#f4f4f4").grid(row=0, sticky="e", padx=10, pady=5)
    tk.Label(airport_gui, text="Location", font=header_font, bg="#f4f4f4").grid(row=1, sticky="e", padx=10, pady=5)
    tk.Label(airport_gui, text="Code", font=header_font, bg="#f4f4f4").grid(row=2, sticky="e", padx=10, pady=5)
    tk.Label(airport_gui, text="Capacity", font=header_font, bg="#f4f4f4").grid(row=3, sticky="e", padx=10, pady=5)

    name_entry = tk.Entry(airport_gui, font=entry_font)
    location_entry = tk.Entry(airport_gui, font=entry_font)
    code_entry = tk.Entry(airport_gui, font=entry_font)
    capacity_entry = tk.Entry(airport_gui, font=entry_font)

    name_entry.grid(row=0, column=1, padx=10, pady=5)
    location_entry.grid(row=1, column=1, padx=10, pady=5)
    code_entry.grid(row=2, column=1, padx=10, pady=5)
    capacity_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Button(airport_gui, text="Submit", command=submit, bg="#4CAF50", fg="white", font=header_font).grid(row=4, columnspan=2, pady=15)

    airport_gui.mainloop()

if __name__ == "__main__":
    # Uncomment the function you want to run
    create_flight_gui()
    # create_airplane_gui()
    # create_booking_gui()
    # create_passenger_gui()
    # create_airport_gui()


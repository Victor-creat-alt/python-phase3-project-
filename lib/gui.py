import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style
from tkinter import ttk
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Flight, Booking, Airplane

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
    flight_gui.geometry("700x600")  # Increase the window size
    style = Style(theme='flatly')  # Use the flatly theme from ttkbootstrap

    # Configure window to center elements
    flight_gui.grid_rowconfigure(0, weight=1)
    flight_gui.grid_rowconfigure(1, weight=1)
    flight_gui.grid_rowconfigure(2, weight=1)
    flight_gui.grid_rowconfigure(3, weight=1)
    flight_gui.grid_rowconfigure(4, weight=1)
    flight_gui.grid_rowconfigure(5, weight=1)

    flight_gui.grid_columnconfigure(0, weight=1)
    flight_gui.grid_columnconfigure(1, weight=3)

    header_font = ("Helvetica", 20)  # Increased font size for title
    entry_font = ("Helvetica", 16)  # Increased font size for entries
    button_font = ("Helvetica", 16)  # Increased font size for button

    # Labels
    ttk.Label(flight_gui, text="Flight Number", font=header_font).grid(row=0, sticky="e", padx=20, pady=10)
    ttk.Label(flight_gui, text="Departure Time (YYYY-MM-DD HH:MM)", font=header_font).grid(row=1, sticky="e", padx=20, pady=10)
    ttk.Label(flight_gui, text="Arrival Time (YYYY-MM-DD HH:MM)", font=header_font).grid(row=2, sticky="e", padx=20, pady=10)
    ttk.Label(flight_gui, text="Destination", font=header_font).grid(row=3, sticky="e", padx=20, pady=10)
    ttk.Label(flight_gui, text="Airplane ID", font=header_font).grid(row=4, sticky="e", padx=20, pady=10)

    # Entry fields (increased size)
    flight_number_entry = ttk.Entry(flight_gui, font=entry_font, width=30)
    departure_time_entry = ttk.Entry(flight_gui, font=entry_font, width=30)
    arrival_time_entry = ttk.Entry(flight_gui, font=entry_font, width=30)
    destination_entry = ttk.Entry(flight_gui, font=entry_font, width=30)
    airplane_id_entry = ttk.Entry(flight_gui, font=entry_font, width=30)

    # Position entry fields
    flight_number_entry.grid(row=0, column=1, padx=20, pady=10)
    departure_time_entry.grid(row=1, column=1, padx=20, pady=10)
    arrival_time_entry.grid(row=2, column=1, padx=20, pady=10)
    destination_entry.grid(row=3, column=1, padx=20, pady=10)
    airplane_id_entry.grid(row=4, column=1, padx=20, pady=10)

    # Submit button (using tk.Button)
    tk.Button(flight_gui, text="Submit", command=submit, width=25, font=button_font).grid(row=5, columnspan=2, pady=20)

    # Set the background color to blue
    flight_gui.config(bg="blue")

    flight_gui.mainloop()

# Function to create a Booking GUI with added styling
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
        messagebox.showinfo("Success", "The booking has been made successfully")

    booking_gui = tk.Tk()
    booking_gui.title("Create Booking")
    booking_gui.geometry("700x600")  # Increase the window size
    style = Style(theme='flatly')  # Use the flatly theme from ttkbootstrap

    # Configure window to center elements
    booking_gui.grid_rowconfigure(0, weight=1)
    booking_gui.grid_rowconfigure(1, weight=1)
    booking_gui.grid_rowconfigure(2, weight=1)
    booking_gui.grid_rowconfigure(3, weight=1)
    booking_gui.grid_rowconfigure(4, weight=1)
    booking_gui.grid_rowconfigure(5, weight=1)

    booking_gui.grid_columnconfigure(0, weight=1)
    booking_gui.grid_columnconfigure(1, weight=3)

    header_font = ("Helvetica", 20)  # Increased font size for title
    entry_font = ("Helvetica", 16)  # Increased font size for entries
    button_font = ("Helvetica", 16)  # Increased font size for button

    # Labels
    ttk.Label(booking_gui, text="Flight ID", font=header_font).grid(row=0, sticky="e", padx=20, pady=10)
    ttk.Label(booking_gui, text="Passenger ID", font=header_font).grid(row=1, sticky="e", padx=20, pady=10)
    ttk.Label(booking_gui, text="Seat Number", font=header_font).grid(row=2, sticky="e", padx=20, pady=10)
    ttk.Label(booking_gui, text="Booking Date (YYYY-MM-DD HH:MM)", font=header_font).grid(row=3, sticky="e", padx=20, pady=10)

    # Entry fields (increased size)
    flight_id_entry = ttk.Entry(booking_gui, font=entry_font, width=30)
    passenger_id_entry = ttk.Entry(booking_gui, font=entry_font, width=30)
    seat_number_entry = ttk.Entry(booking_gui, font=entry_font, width=30)
    booking_date_entry = ttk.Entry(booking_gui, font=entry_font, width=30)

    # Position entry fields
    flight_id_entry.grid(row=0, column=1, padx=20, pady=10)
    passenger_id_entry.grid(row=1, column=1, padx=20, pady=10)
    seat_number_entry.grid(row=2, column=1, padx=20, pady=10)
    booking_date_entry.grid(row=3, column=1, padx=20, pady=10)

    # Submit button (using tk.Button)
    tk.Button(booking_gui, text="Submit", command=submit, width=25, font=button_font).grid(row=4, columnspan=2, pady=20)

    # Set the background color to blue
    booking_gui.config(bg="blue")

    booking_gui.mainloop()

# Function to create an Airplane GUI with added styling
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
        messagebox.showinfo("Success", "The airplane has been created successfully")

    airplane_gui = tk.Tk()
    airplane_gui.title("Create Airplane")
    airplane_gui.geometry("700x600")  # Increase the window size
    style = Style(theme='flatly')  # Use the flatly theme from ttkbootstrap

    # Configure window to center elements
    airplane_gui.grid_rowconfigure(0, weight=1)
    airplane_gui.grid_rowconfigure(1, weight=1)
    airplane_gui.grid_rowconfigure(2, weight=1)
    airplane_gui.grid_rowconfigure(3, weight=1)
    airplane_gui.grid_rowconfigure(4, weight=1)
    airplane_gui.grid_rowconfigure(5, weight=1)

    airplane_gui.grid_columnconfigure(0, weight=1)
    airplane_gui.grid_columnconfigure(1, weight=3)

    header_font = ("Helvetica", 20)  # Increased font size for title
    entry_font = ("Helvetica", 16)  # Increased font size for entries
    button_font = ("Helvetica", 16)  # Increased font size for button

    # Labels
    ttk.Label(airplane_gui, text="Model", font=header_font).grid(row=0, sticky="e", padx=20, pady=10)
    ttk.Label(airplane_gui, text="Capacity", font=header_font).grid(row=1, sticky="e", padx=20, pady=10)
    ttk.Label(airplane_gui, text="Airline", font=header_font).grid(row=2, sticky="e", padx=20, pady=10)
    ttk.Label(airplane_gui, text="Manufacture Year", font=header_font).grid(row=3, sticky="e", padx=20, pady=10)

    # Entry fields (increased size)
    model_entry = ttk.Entry(airplane_gui, font=entry_font, width=30)
    capacity_entry = ttk.Entry(airplane_gui, font=entry_font, width=30)
    airline_entry = ttk.Entry(airplane_gui, font=entry_font, width=30)
    manufacture_year_entry = ttk.Entry(airplane_gui, font=entry_font, width=30)

    # Position entry fields
    model_entry.grid(row=0, column=1, padx=20, pady=10)
    capacity_entry.grid(row=1, column=1, padx=20, pady=10)
    airline_entry.grid(row=2, column=1, padx=20, pady=10)
    manufacture_year_entry.grid(row=3, column=1, padx=20, pady=10)

    # Submit button (using tk.Button)
    tk.Button(airplane_gui, text="Submit", command=submit, width=25, font=button_font).grid(row=4, columnspan=2, pady=20)

    # Set the background color to blue
    airplane_gui.config(bg="blue")

    airplane_gui.mainloop()

if __name__ == "__main__":
    create_flight_gui()  # Call this function to create the Flight GUI
    # You can also call create_booking_gui() or create_airplane_gui() similarly based on what you want to open.

AIR TRAVEL MANAGEMENT SYSTEM
OBJECT RELATIONSHIPS
The Domain Model consists of the following:
  => Captain
  :captain_id(Primary Key)
  :first_name
  :last_name
  :license_number
  :airplane_id(Foreign Key)

  => Passengers
  :passenger_id(Primary Key)
  :first_name
  :last_name
  :email
  :passport_number

  => Airplane
  :airplane_id(Primary Key)
  :model
  :capacity
  :airline
  :manufacture_year

  => Flight 
  :flight_id(Primary Key)
  :flight_number
  :departure_time
  :arrival_time
  :destination
  :airplane_id(Foreign Key)
  :airport_id(Fporeign Key)

  => Bookings
  :booking_id(Primary Key)
  :flight_id(Foreign Key)
  :passenger_id(Foreign Key)
  :seat_number
  :booking_date

ONE TO ONE RELATIONSHIP 
=> An Airplane belongs to a captain

ONE TO MANY RELATIONSHIP
 => An Airplane can have many flights
 => A Flight can be done on many Airports
 => A Flight can have many bookings

MANY TO MANY RELATIONSHIP
 => Several flights can have many passengers 

To use  the Graphical user Interface Application type in the command:
python gui.py
Information is saved in the database based on the function which is uncommented(last line of the code snippet)

To use the command Line Interface Application run:
python command-line.py
Information is saved in the database when one interacts with the Command Line Interface Application and performs CRUD Operations

To seed the database type in the command
python seed.py
Once you enter the ipdb shell run the command seed_database() and information is generated in the database

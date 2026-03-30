"""
Program: HoangNam.Bui.Flight Booking System.py
Student Name: Hoang Nam Bui, Mehak
Course: CPRG 216 - Object-Oriented Programming 1
Assignment: Functions, Scoping and Abstraction
Date: 2026-03-19
"""



import os
MENU_OPTIONS = ["1", "2", "3", "4", "5"]


# flights: list of dictionaries (each dict: flight_no, source, dest, seats, price)
# bookings: list of strings in format "passenger_name,flight_no,seats_booked"

def load_flights(file_name):
    flights = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 5:
                        flight = {
                            'flight_no': parts[0].strip(),
                            'source': parts[1].strip(),
                            'dest': parts[2].strip(),
                            'seats': int(parts[3].strip()),
                            'price': float(parts[4].strip())
                        }
                        flights.append(flight)
        return flights
    except FileNotFoundError:
        return None  # file not found

def save_flights(file_name, flights):

    with open(file_name, 'w') as file:
        for flight in flights:
            line = f"{flight['flight_no']},{flight['source']},{flight['dest']},{flight['seats']},{flight['price']:.2f}\n"
            file.write(line)

def view_flights(flights):
    print("\n" + "-" * 43)
    print(" AVAILABLE FLIGHTS")
    print("-" * 43)
    print(f"{'Flight':<8} {'From':<6} {'To':<6} {'Seats':>6} {'Price':>10}")
    print("-" * 43)
    for flight in flights:
        print(f"{flight['flight_no']:<8} {flight['source']:<6} {flight['dest']:<6} {flight['seats']:>6} ${flight['price']:>8.2f}")
    print("-" * 43)

def view_bookings(passenger_name, bookings):
    print(f"\nBookings for {passenger_name}")
    found = False
    for booking in bookings:
        parts = booking.split(',')
        if len(parts) == 3 and parts[0].strip() == passenger_name:
            print(f"Flight No: {parts[1]}, Seats Booked: {parts[2]}")
            found = True
    if not found:
        print("You have no bookings.")

def book_flight(passenger_name, file_name, flights, bookings):
    flight_no = input("Enter the flight number to book: ").strip().upper()
    flight_found = None
    for flight in flights:
        if flight['flight_no'] == flight_no:
            flight_found = flight
            break
    if flight_found is None:
        print("Flight not found.")
        return
    
    try:
        seats_needed = int(input(f"How many seats would you like to book on {flight_no}? "))
    except ValueError:
        print("Invalid number of seats.")
        return
    
    if seats_needed <= 0:
        print("Invalid number of seats.")
        return
    
    if seats_needed > flight_found['seats']:
        print("Not enough seats available.")
        return
    
    flight_found['seats'] -= seats_needed
    
    save_flights(file_name, flights)

    booking_str = f"{passenger_name},{flight_no},{seats_needed}"
    bookings.append(booking_str)
    
    print(f"Successfully booked {seats_needed} seats on flight {flight_no}.")

def cancel_booking(passenger_name, file_name, flights, bookings):
    flight_no = input("Enter the flight number to cancel: ").strip().upper()
    booking_to_remove = None
    for booking in bookings:
        parts = booking.split(',')
        if len(parts) == 3 and parts[0].strip() == passenger_name and parts[1].strip() == flight_no:
            booking_to_remove = booking
            break
    
    if booking_to_remove is None:
        print("No booking found for the given flight number.")
        return
    

    parts = booking_to_remove.split(',')
    seats_to_cancel = int(parts[2].strip())
    
    flight_found = None
    for flight in flights:
        if flight['flight_no'] == flight_no:
            flight_found = flight
            break
    
    if flight_found:
        flight_found['seats'] += seats_to_cancel
        save_flights(file_name, flights)
        bookings.remove(booking_to_remove)
        print(f"Successfully canceled booking for flight {flight_no}.")
    else:
        print("Error: Flight not found in flight list.")

def main_menu():
    print("\n1. View Available Flights")
    print("2. View My Bookings")
    print("3. Book a Flight")
    print("4. Cancel a Booking")
    print("5. Exit")
    choice = input("Choose an option: ").strip()
    return choice

def main():
    print("-" * 43)
    print(" Flight Booking System")
    print("-" * 43)
    

    while True:
        file_name = input("Enter the flight data file name (e.g., flights.txt): ").strip()
        flights = load_flights(file_name)
        if flights is not None:
            break
        print(f"{file_name} file is not found.")
    
    print("Loading flight data...")
    print(f"Loaded {len(flights)} flights successfully.")
    

    passenger_name = input("Enter the passenger name: ").strip()
    

    bookings = []
    while True:
        choice = main_menu()
        
        if choice == "1":
            view_flights(flights)
        elif choice == "2":
            view_bookings(passenger_name, bookings)
        elif choice == "3":
            book_flight(passenger_name, file_name, flights, bookings)
        elif choice == "4":
            cancel_booking(passenger_name, file_name, flights, bookings)
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

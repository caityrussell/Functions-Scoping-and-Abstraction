def view_flights(flights_list):
    '''
    function name: view_flights()
    description: opens file with flight information and displays in a tabular format
    parameters: (file) containing flight information
    returns: does not return any value
    '''

    # display table header
    print(f"-"*40)
    print(f"{'AVAILABLE FLIGHTS':^40}")
    print(f"-"*40)
    print(f"{'Flight':<10}{'From':<8}{'To':<6}{'Seats':<8}{'Price':<10}")
    print(f"-"*40)
    
    for flight in flights_list:
            print(f"{flight[0]:<10}{flight[1]:<8}{flight[2]:<6}{flight[3]:<8}${float(flight[4]):<10.2f}")
    # display table footer
    print(f"-"*40)

def book_flight(passenger_name, file_name, flights_list, bookings_list):
    '''
    function name: book_flights()
    description: user inputs flight number function checks file 
    if flight exits user selects number of seats and flight booking is confirmed
    parameters: (file) containing passenger name, file name, and flight list
    returns: does not return any value
    '''

    # ask user to input flight number
    flight_num = input('Enter flight number to book: ')
    
    # set flight found flag to false
    flight_found = False

    # loops through flight list
    for flight in flights_list:
        
        # checks to see if flight number exists
        if flight[0] == flight_num:
            # set flight found flag to true
            flight_found = True
            # ask user to input number of seats and checks availability
            seat_num = int(input(f"How many seats would you like to book on {flight_num}? "))
            seat_avail = int(flight[3])
            if seat_num <= seat_avail:
                # stores new number of available seats into a list
                new_seats = seat_avail - seat_num
                flight[3] = str(new_seats)

                # call save flights function
                save_flights(file_name, flights_list)

                # adds booking to booking list
                booking_info = passenger_name + "," + flight_num + "," + str(seat_num)
                bookings_list.append(booking_info)
                print(f"Successfully booked {seat_num} seats on {flight_num}.")
            else:
                print('Not enough seats available.')

    # error message if flight is not found 
    if flight_found == False:
        print('Flight not found.')

def view_bookings(passenger_name, bookings_list):
    '''
    function name: view_bookings()
    description: iterates through the bookings list and displays all flights
    and seats booked for the current passenger
    parameters: passenger_name (string) - name of the current passenger
    bookings_list (list) - list of all booking strings
    returns: does not return any value
    '''
    
    # display booking header for passengers name
    print(f"Bookings for {passenger_name}")

    bookings_found = False

    # search through bookings list and sort into a list
    for booking in bookings_list:
        booking_info = booking.strip().split(",")

        # assign variable names to list items using index
        name = booking_info[0]
        flight_no = booking_info[1]
        seats = booking_info[2]

        # check to see if passenger name exists in bookings list
        if name == passenger_name:
            # set bookings found flag to true
            bookings_found = True
            # display flight number and seats booked
            print(f"Flight No: {flight_no}, Seats Booked: {seats}")
    
    # display user has no bookings if name not found in list
    if bookings_found == False:
        print(f"You have no Bookings")

def cancel_booking(passenger_name, file_name, flights_list, bookings_list):
    '''
    function name: cancel_booking()
    description: searches the bookings list for a matching flight number and
    cancels the booking by removing it from the bookings list and
    returning the seats back to the flights list, then saves the
    updated flight data to the flights file
    parameters: passenger_name (string) - name of the current passenger
    file_name (string) - name of the flights file
    flights_list (list) - list of all available flights
    bookings_list (list) - list of all current bookings
    returns: does not return any value
    '''
    flight_no = input('Enter flight number to cancel: ')

    booking_found = False

    for booking in bookings_list:
        booking_info = booking.strip().split(",")

        # assign variable names to list items using index
        name = booking_info[0]
        flight_number = booking_info[1]
        seats = booking_info[2]


        # check if flight number exists
        if flight_no == flight_number:
            booking_found = True
            return_seats = int(seats)

            # update flight
            for flight in flights_list:  
                if flight[0] == flight_no:
                    flight[3] = int(flight[3]) + return_seats 
                    flight[3] = str(flight[3])      

                    # call save flights function
                    save_flights(file_name, flights_list)

                    # remove booking from booking_list
                    bookings_list.remove(booking)

                    # display booking success message once flight is cancelled
                    print(f"Successfully canceled booking for flight {flight_no}")

    # error message if booking not found
    if booking_found == False:
        print('No booking found for the given flight number.')

def load_flights(file_name):
    '''
    function name: load_flights
    description: reads data front the flight file and stores into a list
    parameters: (file) containing flight information
    returns: flight list
    '''

    flights_list = []

    with open(file_name, 'r') as file:
            # loop through file lines, split into list, and display values using their indexes
            for line in file:
                data = line.strip().split(",")
                flights_list.append(data)
    
    return flights_list

def save_flights(file_name, flights_list):
    '''
    function name: save_flights()
    description: saves the updated flights list to the flights file
    formatted as comma separated values
    parameters: file_name (string) - name of the flights file
    flights_list (list) - list of all available flights
    returns: does not return any value
    '''

    # open file for writing
    with open(file_name, "w") as file:
        # loop through items in flight list
        for flight in flights_list:
            # seperate items by comma and write to file
            file.write(",".join(flight) + "\n")

def main_menu():
    '''
    function name: main_menu()
    description: displays menu options and asks user to input their selection
    parameters: none
    returns: option (integer) - the user's menu selection
    '''
    print(f"\n1. View Available Flights")
    print("2. View My Bookings")
    print("3. Book a Flight")
    print("4. Cancel a Booking")
    print("5. Exit")

    option = int(input("Choose an option: "))

    return option     

def main():
    # display welcome banner
    print(f"-"*40)
    print(f"{'Flight Booking System':^40}")
    print(f"-"*40)
    file_name = input("Enter the flight data file name (e.g), flights.txt: ")

    import os

    while os.path.exists(file_name) == False:
        print(f"{file_name} file is not found")
        file_name = input("Enter the flight data file name (e.g), flights.txt: ")

    print("Loading flight data...")
    flights_list = load_flights(file_name)
    bookings_list = []
    num_flights = len(flights_list)
    print(f"Loaded {num_flights} flights successfully")
    passenger_name = input("Enter the passenger name: ")

    option = main_menu()

    while option != (5):
        if option == 1:
            view_flights(flights_list)
        elif option == 2:
            view_bookings(passenger_name, bookings_list)
        elif option ==3:
            book_flight(passenger_name, file_name, flights_list, bookings_list)
        elif option == 4:
            cancel_booking(passenger_name, file_name, flights_list, bookings_list)
        else:
            print('Invalid option. Please try again.')

        option = main_menu()

    print('Exiting the system. Goodbye!')

main()
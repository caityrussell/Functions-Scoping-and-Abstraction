
'''
    Program Name: Functions.py
    Authors: Caitlyn, Nam, Mehakpreet, Ali
    date: 26-Mar-2026
    Description: Program to book flight for user, disply flight detalis
                 and cancel flight.


'''

# variable details:
# file_name (input file name from user)
# passenger_name (passenger name)
# menu (a tuple to store menu items)
# option_selected (option selected by user from given menu)
# flights_lists = parameter passed to function (view_flights)
# flights_available = a dict to store flight name and no of seats



globalflights_list = {}
def view_flights(flights_list):
    print('-'*42,'\n\tAVAILABLE FLIGHTS\n','-'*42)
    with open(flights_list) as f:
        print(f'flights','From','To','Seats','Price',sep=' '*4)
        for line in f:
            line = line.rstrip()
            print(line.replace(',', '\t   '))
    print('-'*42)
    return 
    


def view_bookings(passenger_name,bookings_list):
    print(bookings_list)
    print(f'Bookings for {bookings_list['name']}')
    for key, value in bookings_list.items():
        if key == "name":
            continue
        print(f'Flight No: {key}, Seats Booked: {value}')



def cancel_booking(booking_lists):
    flight_no = input("enter the flight number to cancel ")


    if flight_no in booking_lists:
        del booking_lists[flight_no]
    else:
        print('No booking found for the given flight number ')
    


def book_flight(passenger_name,file_name,bookings_list):
    
    flights_list = {}
    with open (file_name) as f:
        for line in f:
            val = line.strip().split(',')
            flight_number = val[0]
            seats=int(val[3])       
            flights_list[flight_number]= seats 
        print(flights_list)
    
    flight_number = input("Enter the flight number to book: ")
    if flight_number in flights_list:
        
        booked_seats = int(input(f'How many seats would you like to book on {flight_number}? '))
        if booked_seats < flights_list[flight_number]:
            # print(flights_list[flight_number])
            bookings_list.update({flight_number : booked_seats})
            seats_left = flights_list[flight_number] - booked_seats
            save_flights(flight_number,seats_left,file_name)
            print(f'Successfully booked {booked_seats} seats on flight {flight_number}')
            
        else:
            print('Not enough seats available')
    else:
        print('Flight not found')
    
    
    print(bookings_list)






def save_flights(flight_number,seats_left,file_name):
    with open (file_name,) as f:
        # line = f.readline()

        for line  in f:
            items = line.rstrip().split(',')
            if items[0] == flight_number:
                items[3]=seats_left
                print(items[3])
            

def main_menu():
    menu = ('\n1. View Available Flights',
          '2. View My Bookings',
          '3. Book a Flight',
          '4. Cancel a Booking',
          '5. Exit')
    for items in menu:
        print(items)
    option_selected = int(input('Choose an option: '))
    while   option_selected<=0 or option_selected >=6:
        print('Invalid option. Please try again')
        for items in menu:
            print(items)
        option_selected = int(input('Choose an option: '))
    return option_selected
    

def main():
    
   
    import os
    print('-'*42,'\n\tFlight Booking System\n','-'*42)
    file_name = input('Enter the flight data file name (e.g flights.txt): ')
    if os.path.exists(file_name):
        print('Loading flight data...')
        print('Loaded 5 flights successfully.')
    else:
        while(file_name != 'flights.txt'):
            print(f'{file_name} file is not find')
            file_name = input('Enter the flight data file name (e.g flights.txt): ')
            if os.path.exists(file_name):
                print('Loading flight data...')
                print('Loaded 5 flights successfully.')
    passenger_name = input('Enter the passenger name: ')

    

    option_selected = main_menu()
    bookings_list = {'name':passenger_name}
   
    while 0<=option_selected <=6:
        # option_selected = input('Choose an option')
        match option_selected:
            case 1:
             
             file_name = 'flights.txt'
             view_flights(file_name)
             option_selected = main_menu()


            case 2:
                view_bookings(passenger_name,bookings_list)
                option_selected = main_menu()

            case 3:
                book_flight(passenger_name,file_name,bookings_list)
                option_selected = main_menu()

            case 4:
                print('You entered match-case 4')
                print('for cancel booking')
                cancel_booking(bookings_list)
                option_selected = main_menu()
            
            case 5:
                print('Exiting the system.Goodbye!')
                break
    
main()

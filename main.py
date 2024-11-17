import argparse
from test_selenium import LibraryBooking

def main():
    #input id & password
    username = input("Enter your EdUHK username: ")
    password = input("Enter your EdUHK password: ")
    #Inqire the area  
    area = input("There are there areas that you can choose to book,\nplease press the number below to choose\n 1: '4/F Research Commons A'\n 2:'4/F Research Commons B'\n 3: 'G/F Quiet Zone & PC Area'\n")
    booking = LibraryBooking(username, password) 
    
    try:
        if booking.login():

            #Choose area
            while True:
                if area == 1:
                    available_seats = booking.find_available_seat('4/F Research Commons A')
                    break
                elif area == 2:
                    available_seats = booking.find_available_seat('4/F Research Commons B')
                    break
                elif area == 3:
                    available_seats = booking.find_available_seat('G/F Quiet Zone & PC Area')
                    break
                else: 
                    print("\nIncorrect input of area. You can only input 1, 2 or 3\n")
                    break
            
            # Check current bookings
            
            
            if available_seats:
                 print("Available seats:")
            for seat, time_slots in available_seats.items():
                print(f"Seat: {seat}, Available time slots: {', '.join(time_slots)}")
        else:
            print("No available seats found.")
   
    except Exception as e:
        print(f"An error occurred in main program: {e}")
    
    finally:
        booking.close()

import argparse
from test_selenium import LibraryBooking
import time

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
                    booking.book_seat('4/F Research Commons A')
                    break
                elif area == 2:
                    booking.book_seat('4/F Research Commons B')
                    break
                elif area == 3:
                    booking.book_seat('G/F Quiet Zone & PC Area')
                    break
                else: 
                    print("\nIncorrect input of area.\n")
                    break
            
            # Check current bookings
            if booking.login():
            
                my_bookings = booking.check_my_bookings()
            
                if my_bookings:
                    print("\n--- All your current bookings ---")
                    print(f"Total: {my_bookings['total_bookings']}")
                    
                    # Detailed bookings
                    for idx, booking in enumerate(my_bookings['bookings'], 1):
                        print(f"\nBooking {idx}:")
                        print(f"Start time: {booking['start_time']} - {booking['end_time']}")
                        print(f"Area: {booking['area']}")
                        print(f"Location: {booking['location']}")
                        print(f"Status: {booking['status']}")
                        print(f"Latest update: {booking['last_updated']}")
                        if booking['cancel_link']:
                            print(f"cancel link: {booking['cancel_link']}")
    
    except Exception as e:
        print(f"An error occurred in main program: {e}")
    
    finally:
        booking.close()

if __name__ == "__main__":
    main()


"""
If you forget your EdUHK Network Password, please contact "https://www.eduhk.hk/ocio/contact-us" for assistance.
"""
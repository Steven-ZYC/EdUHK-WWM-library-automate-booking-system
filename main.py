import argparse
from test_selenium import LibraryBooking

def main():
    #input id & password
    username = input("Enter your EdUHK username: ")
    password = input("Enter your EdUHK password: ")
    booking = LibraryBooking(username, password)
    
    

    try:
        if booking.login():

            #area
            while True:
                area = input("There are there areas that you can choose to book,\nplease press the number below to choose\n 1: '4/F Research Commons A'\n 2:'4/F Research Commons B'\n 3: 'G/F Quiet Zone & PC Area'")
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
                    print("Incorrect input.")
            
            # Check current bookings
            my_bookings = booking.check_my_bookings()
            if my_bookings:
                print(f"Unchecked bookings: {len(my_bookings['unchecked_bookings'])}")
                print(f"Checked bookings: {len(my_bookings['checked_bookings'])}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        booking.close()

if __name__ == "__main__":
    main()


"""
If you forget your EdUHK Network Password, please contact "https://www.eduhk.hk/ocio/contact-us" for assistance.
"""
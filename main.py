import getpass
import time
from test_selenium import LibraryBooking
from datetime import datetime, timedelta

def main():

    try:
        #input id & password
        username = input("Enter your EdUHK SID: ")
        password = getpass.getpass("Enter your EdUHK password: (Your input wouldn't display)")
        #Inqire the area  
        area = input("There are there areas that you can choose to book,\nplease press the number below to choose\n 1: '4/F Research Commons A'\n 2:'4/F Research Commons B'\n 3: 'G/F Quiet Zone & PC Area'\n")
        
        booking = LibraryBooking(username, password) 
    
        try:
            if booking.login():

                #Choose area
                while True:
                    if area == "1":
                        seat_area = '4/F Research Commons A'
                        break
                    elif area == "2":
                        seat_area = '4/F Research Commons B'
                        break
                    elif area == "3":
                        seat_area = 'G/F Quiet Zone & PC Area'
                        break
                    else: 
                        print("\nIncorrect input of area. You can only input 1, 2 or 3\n")
                        return False

                available_seats = booking.find_available_seat(seat_area)
                # Check current bookings
                
                
                if available_seats:
                    print("Select output mode:\n1. Top 5 available seats\n2. All available seats")
                    mode = input("Enter 1 or 2:\n ")

                    print(f"Seat number:{"1":^24}{"2":^15}{"3":^15}{"4":^15}{"5":^15}{"6":^15}{"7":^15}{"8":^15}{"9":^15}{"10":^15}")
                    print("Available seats:")
                    if mode == "1":
                        max_output = 5

                    elif mode == "2":  
                        max_output = 60

                    for i, (seat, details) in enumerate(available_seats.items(), start=1):
                        print(f"Seat: {seat}")
                        print(f"Available time slots: {', '.join(details['time_slots'][1:])}")
                        print()        
                        if i == max_output:
                            break
                    else:
                        print("Incorrect input of mode")

                
                    seat_name = str(input("Then choose the seat you want to book (full name reqired e.g S57 (With PC))\n"))
                    print("Seat name entered:", seat_area)
                    print("Seat name entered:", seat_name)

                    for n in range(1,13):
                        print(f"Attempting to book time slot {n}...")
                        booking.booking_seats(seat_area,seat_name,n)    
                    
                            
                else:
                    print("No available seats found.")
            
                time.sleep(1)
            
                checkin = booking.check_in()

                if checkin:
                    print("Detect that you are using the workstation in library\n You are cheked in！")


        except Exception as e:
            print(f"An error occurred in main program: {e}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        booking.close()


if __name__ == "__main__":
    main()
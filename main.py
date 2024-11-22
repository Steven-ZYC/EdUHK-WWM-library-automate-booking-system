import getpass
import time
from test_selenium import LibraryBooking
from datetime import datetime, timedelta
import threading

def attempt_booking(booking, seat_area, seat_name, time_slot_index):
    """Function to attempt booking in a separate thread."""
    print(f"Attempting to book time slot {time_slot_index}...")
    success = booking.booking_seats(seat_area, seat_name, time_slot_index)
    if success:
        # Only create ICS file if booking is successful
        start_time_str = booking.available_seats[seat_name]['time_slots'][time_slot_index - 1]
        start_time = datetime.strptime(start_time_str, "%H:%M")
        start_time = start_time.replace(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
        duration = 120  # Set duration to 120 minutes
        end_time = start_time + timedelta(minutes=duration)
        

def main():
    try:
        # Input ID & password
        username = input("Enter your EdUHK SID: ")
        password = getpass.getpass("Enter your EdUHK password: (Your input wouldn't display)")
        # Inquire the area  
        area = input("There are three areas that you can choose to book,\nplease press the number below to choose\n 1: '4/F Research Commons A'\n 2: '4/F Research Commons B'\n 3: 'G/F Quiet Zone & PC Area'\n")
        
        booking = LibraryBooking(username, password) 
    
        if booking.login():
            # Choose area
            if area == "1":
                seat_area = '4/F Research Commons A'
            elif area == "2":
                seat_area = '4/F Research Commons B'
            elif area == "3":
                seat_area = 'G/F Quiet Zone & PC Area'
            else: 
                print("\nIncorrect input of area. You can only input 1, 2 or 3\n")
                return False

            available_seats = booking.find_available_seat(seat_area)
            
            if available_seats:
                print("Select output mode:\n1. Top 5 available seats\n2. All available seats")
                mode = input("Enter 1 or 2:\n ")

                print(f"Seat number:{"1":^24}{"2":^15}{"3":^15}{"4":^15}{"5":^15}{"6":^15}{"7":^15}{"8":^15}{"9":^15}{"10":^15}")
                print("Available seats:")
                max_output = 5 if mode == "1" else 50 if mode == "2" else 0

                for i, (seat, details) in enumerate(available_seats.items(), start=1):
                    print(f"Seat: {seat}")
                    print(f"Available time slots: {', '.join(details['time_slots'][1:])}")
                    print()        
                    if i == max_output:
                        break
                
                seat_name = str(input("Then choose the seat you want to book (full name required e.g S57 (With PC))\n"))
                print("Seat name entered:", seat_area)
                print("Seat name entered:", seat_name)

                threads = []
                for n in range(1, 12):
                    thread = threading.Thread(target=attempt_booking, args=(booking, seat_area, seat_name, n))
                    threads.append(thread)
                    thread.start()

                for thread in threads:
                    thread.join()  # waiting for completion of threads.
            
            else:
                print("No available seats found.")
            
            time.sleep(1)
            checkin = booking.check_in()

            if checkin:
                print("Detect that you are using the workstation in library\nYou are checked in！")

    except Exception as e:
        print(f"An error occurred in main program: {e}")

    finally:
        booking.close()

if __name__ == "__main__":
    main()
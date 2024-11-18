import getpass
from test_selenium import LibraryBooking

def main():
    #input id & password
    username = input("Enter your EdUHK username: ")
    password = getpass.getpass("Enter your EdUHK password: (Your input wouldn't display)")
    #Inqire the area  
    area = input("There are there areas that you can choose to book,\nplease press the number below to choose\n 1: '4/F Research Commons A'\n 2:'4/F Research Commons B'\n 3: 'G/F Quiet Zone & PC Area'\n")
    booking = LibraryBooking(username, password) 
    
    try:
        if booking.login():

            #Choose area
            while True:
                if area == "1":
                    available_seats = booking.find_available_seat('4/F Research Commons A')
                    break
                elif area == "2":
                    available_seats = booking.find_available_seat('4/F Research Commons B')
                    break
                elif area == "3":
                    available_seats = booking.find_available_seat('G/F Quiet Zone & PC Area')
                    break
                else: 
                    print("\nIncorrect input of area. You can only input 1, 2 or 3\n")
                    break
            
            # Check current bookings
            
            
            if available_seats:
                print("Select output mode:\n1. Top 5 available seats\n2. All available seats")
                mode = input("Enter 1 or 2:\n ")

                print("Available seats:")
                if mode == "1":
                    max_output = 5
                elif mode == "2":
                    max_output = 5
                for i, (seat, details) in enumerate(available_seats.items(), start=1):
                    print(f"Seat: {seat}")
                    print(f"Available time slots: {', '.join(details['time_slots'][1:])}")
                    print()
                    
                    if i == max_output:
                        break

                       
                    print("Available seats:")
                    for seat, time_slots in available_seats.items():
                        print(f"Seat: {seat}, Available time slots: {', '.join(time_slots)}")
                    
                    
                else:
                    print("Incorrect input of mode")
        else:
            print("No available seats found.")
   
    except Exception as e:
        print(f"An error occurred in main program: {e}")
    
    finally:
        booking.close()


if __name__ == "__main__":
    main()
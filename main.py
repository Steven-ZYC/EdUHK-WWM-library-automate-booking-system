from network import Seat, Booking

def main():
    #area = input('Please choose the area that you want to book. "a"for reasearch zone A, "b"for reachearch zone B, "s"for pc workstation\n')
    seat_number = input("Enter seat number (e.g., A1).\nYou can refer to https://www.lib.eduhk.hk/facilities-booking: ")
    seat = Seat(seat_number)
    #area = Seat(seat)
    booking = Booking(seat)

    action = input("Do you want to book or cancel? (b/c): ").strip().lower()

    if action == 'b':
        if booking.book_seat():
            print(f"Seat {seat.seat_number} booked successfully.")
        else:
            print(f"Seat {seat.seat_number} is already booked.")
    elif action == 'c':
        if booking.cancel_booking():
            print(f"Booking for seat {seat.seat_number} canceled.")
        else:
            print(f"No booking found for seat {seat.seat_number}.")
    else:
        print("Invalid action. Please enter 'b' to book or 'c' to cancel.")


if __name__ == "__main__":
    main()





"""
If you forget your EdUHK Network Password, please contact "https://www.eduhk.hk/ocio/contact-us" for assistance.
"""
import requests
from bs4 import BeautifulSoup

url_root = "https://www.lib.eduhk.hk/facilities-booking"
url_a = "https://app.lib.eduhk.hk/booking/day.php?area=1"
url_b = "https://app.lib.eduhk.hk/booking/day.php?area=2"
url_pc = "https://app.lib.eduhk.hk/booking/day.php?area=6"
url_login = "https://app.lib.eduhk.hk/booking/admin.php"

class Seat:
    def __init__(self, area, seat_number):
        #self.area = area
        self.seat_number = seat_number
        self.is_booked = False

class Booking:
    def __init__(self, area, seat):
        self.seat = seat
        #self.area = area 

    def book_seat(self):
        if not self.seat.is_booked:
            self.seat.is_booked = True
            return True
        return False

    def cancel_booking(self):
        if self.seat.is_booked:
            self.seat.is_booked = False
            return True
        return False
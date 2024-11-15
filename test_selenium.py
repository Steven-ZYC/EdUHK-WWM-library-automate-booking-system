from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

class LibraryBooking:
    AREAS = {
        '4/F Research Commons A': 1,
        '4/F Research Commons B': 2,
        'G/F Quiet Zone & PC Area': 6,
        'G/F Discussion Booths': 44
    }


    def __init__(self, username, password):
        # Setup Chrome
        self.chrome_options = webdriver.ChromeOptions()

        # options for headless mode (i.e. uncomment run without opening browser)
        # self.chrome_options.add_argument("--headless")
        
        # Setup webdriver
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), 
            options=self.chrome_options
        )
        # Setup username passwd urls
        self.username = username
        self.password = password
        self.url = "https://app.lib.eduhk.hk/booking/"
        self.url_login = self.url + "admin.php"
        self.books = self.url + "edit_entry.php?"

    def login(self):
        """
        Let user input username and password 
        """
        try:
            # Navigate to login page
            self.driver.get(self.url_login)
            
            # Wait and find username field
            username_field = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, "NewUserName"))
            )
            username_field.clear()  # Clear field before entering new data
            username_field.send_keys(self.username)
            
            # Find and fill password field
            password_field = self.driver.find_element(By.ID, "NewUserPassword")
            password_field.clear()  # Clear field before entering new data
            password_field.send_keys(self.password + Keys.RETURN)
                
            # Wait for login to complete
            WebDriverWait(self.driver, 1).until(
                EC.url_changes(self.url_login)
            )
                
            print("Login successful!")
            return True
            
        except Exception as e:
            print(f'\nLogin failed. \nPlease check your username and password. {e}\nIf you forget your EdUHK Network Password, please contact "https://www.eduhk.hk/ocio/contact-us" for assistance.\n')
            return False

    def find_available_seat(self, area_name):
        """
        Find an available seat in the specified area
        
        :param area_name: Name of the area to book
        :return: WebElement of the available seat or None
        """
        try:
            # Get area number from the dictionary
            area_num = self.AREAS.get(area_name)
            if not area_num:
                print(f"Invalid area name: {area_name}")
                return None

            # Navigate to the area's day view
            self.driver.get(f"{self.url}day.php?area={area_num}")

            # Find available seats (with class 'new')
            available_seats = self.driver.find_elements(By.CLASS_NAME, "new")
            
            if not available_seats:
                print(f"No available seats in {area_name}")
                return None

            # Return the first available seat
            return available_seats[0]

        except Exception as e:
            print(f"Error finding available seat: {e}")
            return None

    def book_seat(self, area_name):
        """
        Book a seat in the specified area
        
        :param area_name: Name of the area to book
        :return: Boolean indicating booking success
        """
        try:
            # Find an available seat
            available_seat = self.find_available_seat(area_name)
            
            if not available_seat:
                return False

            # Click on the available seat
            available_seat.click()

            # Wait for booking form to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "edit_entry"))
            )

            # Submit the booking
            submit_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
            submit_button.click()

            # Wait for confirmation
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "success"))
            )

            print(f"Successfully booked a seat in {area_name}")
            return True

        except Exception as e:
            print(f"Booking failed: {e}")
            # Take a screenshot for debugging
            self.driver.save_screenshot("booking_error.png")
            return False

    def check_my_bookings(self):
        """
        Check current user's bookings
        
        :return: List of current bookings
        """
        try:
            # Navigate to my bookings
            self.driver.get(f"{self.url}my_bookings.php")

            # Find bookings with specific classes
            my_uncheckin_bookings = self.driver.find_elements(
                By.CLASS_NAME, "I.tentative.writable"
            )
            my_checkin_bookings = self.driver.find_elements(
                By.CLASS_NAME, "E.writable"
            )

            # Combine and return bookings
            return {
                'unchecked_bookings': my_uncheckin_bookings,
                'checked_bookings': my_checkin_bookings
            }

        except Exception as e:
            print(f"Error checking bookings: {e}")
            return None
    

    def close(self):
        self.driver.quit()

# For direct script execution
if __name__ == "__main__":
    username = input("Enter your EdUHK username: ")
    password = input("Enter your EdUHK password: ")
    
    booking = LibraryBooking(username, password)
    
    try:
        if booking.login():

            # Book a seat in Quiet Zone & PC Area
            booking.book_seat('G/F Quiet Zone & PC Area')
            
            # Check current bookings
            my_bookings = booking.check_my_bookings()
            if my_bookings:
                print(f"Unchecked bookings: {len(my_bookings['unchecked_bookings'])}")
                print(f"Checked bookings: {len(my_bookings['checked_bookings'])}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        booking.close()
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
    def __init__(self, username, password):
        # Setup Chrome
        self.chrome_options = webdriver.ChromeOptions()

        # options for headless mode (optional)
        # Uncomment below if you want to run without opening browser
        # self.chrome_options.add_argument("--headless")
        
        # Setup webdriver
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), 
            options=self.chrome_options
        )
        
        self.username = username
        self.password = password
        self.base_url = "https://app.lib.eduhk.hk/booking/admin.php"

    def login(self):
        try:
            # Navigate to login page
            self.driver.get(self.base_url)
            
            # Wait and find username field
            username_field = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "NewUserName"))
            )
            username_field.send_keys(self.username)
            
            # Find and fill password field
            password_field = self.driver.find_element(By.ID, "NewUserPassword")
            password_field.send_keys(self.password + Keys.RETURN)
            
            # Find and click login button
            #login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            #login_button.click()
            
            # Wait for login to complete
            WebDriverWait(self.driver, 5).until(
                EC.url_changes(self.base_url)
            )
            
            print("Login successful!")
            return True
        
        except Exception as e:
            print(f"Login failed.Please check your username and password: \n{e}")
            return False

    def book(self):
        try:
            # Navigate to booking page (adjust URL if different)
            self.driver.get(f"{self.base_url}?area=gf_computer_zone")
            
            # Find and click available seat
            available_seat = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".seat-available"))
            )
            available_seat.click()
            
            # Confirm booking
            confirm_button = self.driver.find_element(By.ID, "confirm-booking")
            confirm_button.click()
            
            print("Seat booked successfully!")
            return True
        
        except Exception as e:
            print(f"Booking failed: {e}")
            return False

    def close(self):
        self.driver.quit()

# For direct script execution

   

if __name__ == "__main__":
    username = input("Enter your EdUHK username: ")
    password = input("Enter your EdUHK password: ")
    
    booking = LibraryBooking(username, password)
    
    try:
        if booking.login():
            booking.book_gf_computer_zone()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        booking.close()
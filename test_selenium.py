from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
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
        self.options = webdriver.ChromeOptions()

        # Setup Edge
        # self.options = webdriver.EdgeOptions()

        # self.options.add_argument("--disable-dev-shm-usage")
        # options for headless mode (i.e. uncomment run without opening browser)
        # self.options.add_argument("--headless")
        
        # Setup webdriver
        self.options.add_argument("--force-device-scale-factor=0.75") 
        self.options.add_argument('--log-level=1')
        
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), 
            options=self.options
        )
        
        
        # Setup username passwd urls
        self.username = username
        self.password = password
        self.url = "https://app.lib.eduhk.hk/booking/"
        self.url_login = self.url + "admin.php"
        self.url_area = self.url + "day.php?area="
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
            time.sleep(2)  
            print("Login successful!")
            return True
            
        except Exception as e:
            print(f'\nLogin failed. \nPlease check your username and password. {e}\nIf you forget your EdUHK Network Password, please contact "https://www.eduhk.hk/ocio/contact-us" for assistance.\n')
            return False

    def redirect_to_area(self, area_name):
        """
        Book a seat in the specified area
        
        :param area_name: Name of the area to book
        :return: Boolean indicating booking success
        """
    
        try:
            """
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
            """
            # Wait for navigation bar element to be present
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul/li[1]/a'))
            )
            
            # Hover over and click to expand dropdown menu
            navbar_button = self.driver.find_element(By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul/li[1]/a')
            actions = ActionChains(self.driver)
            actions.move_to_element(navbar_button).perform()
            navbar_button.click()
            
            # Locate and click specific area by name
            try:
                area_element = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, f"//ul[@class='dropdown-menu']//a[contains(text(), '{area_name}')]"))
                )
                area_element.click()
                print(f"Successfully navigated to {area_name}")
                return True
            
            except Exception as e:
                print(f"Area {area_name} not found: {e}")
                return False
    
        except Exception as e:
            print(f"Error navigating to area selection page: {e}")
            return False
        
    def find_available_seat(self, area_name):
        """
        Find all available seats in the specified area.
        
        :param area_name: Name of the area to book
        :return: List of available seat names or None if no seats are available
        """
        try:
            # Get area number from the dictionary
            area_num = self.AREAS.get(area_name)
            if not area_num:
                print(f"Invalid area name: {area_name}")
                return None

            # Navigate to the area's day view
            self.driver.get(f"{self.url}day.php?area={area_num}")

            # Wait for the table to load
            table = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//table[@class='dwm_main_6 footable footable-1 breakpoint-lg' and @id='day_main']"))
            )

            # Find all available seat names
            available_seats = table.find_elements(By.XPATH, "//td[contains(@class, 'new')]")
            seat_names = [seat.get_attribute("data-room") for seat in available_seats]

            if not seat_names:
                print(f"No available seats in {area_name}")
                return None

            return seat_names

        except Exception as e:
            print(f"Error finding available seats: {e}")
            return None
    
    def check_my_bookings(self):
        """
        Check current user's bookings
        :return: List of current bookings
        """

        try:
            # Navigate to my bookings
            element =  WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='bs-example-navbar-collapse-1']/ul/li[5]/a"))
                )
            mybooking = self.driver.find_element(By.XPATH, "//*[@id='bs-example-navbar-collapse-1']/ul/li[5]/a")
            mybooking.click()
            time.sleep(8)
            
            # wait for the table loading
            bookings_table = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "report_table"))
                )
             
            # look for rows and skip the first element
            booking_rows = bookings_table.find_elements(By.TAG_NAME, "tr")[1:]  

            bookings = []

            for row in booking_rows:
                try:
                    cells = row.find_elements(By.TAG_NAME, "td")
                    cancel_link = cells[-1].find_element(By.TAG_NAME, "a") if cells[-1].find_elements(By.TAG_NAME, "a") else None
                    
                    # Create the detailed dictionary  
                    booking_details = {
                        'start_time': cells[0].text.strip(),
                        'end_time': cells[1].text.strip(),
                        'duration': cells[2].text.strip(),
                        'area': cells[3].text.strip(),
                        'location': cells[4].text.strip(),
                        'status': cells[5].text.strip(),
                        'last_updated': cells[6].text.strip(),
                        'cancel_link': cancel_link.get_attribute('href') if cancel_link else None,
                        'cancel_confirmation_text': cancel_link.get_attribute('onclick') if cancel_link else None
                    }

                    bookings.append(booking_details)

                except Exception as row_error:
                    print(f"Error exist when prosess the row: {row_error}")
            return {
            'bookings': bookings,
            'total_bookings': len(bookings)
            }

            
        except Exception as e:
            print(f"Error checking bookings: {e}")
            return None
    

    def close(self):
        self.driver.quit()

# For direct script execution
if __name__ == "__main__":
    
    try:
        username = input("Enter your EdUHK username: ")
        password = input("Enter your EdUHK password: ")

        booking = LibraryBooking(username, password)
        
        if booking.login():
           #booking.redirect_to_area('G/F Quiet Zone & PC Area')
           time.sleep(2) 
           
           booking.find_available_seat('G/F Quiet Zone & PC Area')
            # Check current bookings
           """ 
           my_bookings = booking.check_my_bookings()
            if my_bookings:
                print(f"Unchecked bookings: {len(my_bookings['unchecked_bookings'])}")
                print(f"Checked bookings: {len(my_bookings['checked_bookings'])}")
            """
        time.sleep(5)
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        booking.close()
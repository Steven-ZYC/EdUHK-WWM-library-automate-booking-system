from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Edge WebDriver
driver = webdriver.Edge()
def login(username,password):
    driver.get('https://app.lib.eduhk.hk/booking/admin.php')
    time.sleep(1)  # Wait for the page to load

    # Fill in the login form
    driver.find_element(By.ID, 'NewUserName').send_keys(username)  # Replace with your username
    driver.find_element(By.ID, 'NewUserPassword').send_keys(password + Keys.RETURN)  # Replace with your password

    time.sleep(1)  # Wait

    
    
    login_button = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]')
    please_login_text = driver.find_element(By.CLASS_NAME, 'navbar-brand').text
    
    print(f"button{login_button}")
    print(f"text{please_login_text}")
    if "Log in" in login_button.text and "Please login" in please_login_text:
        print("\nFailed to log in. Please check your ID and password.")
        return False
    else:
        # If we can't find these elements, login was successful
        print("\nLogin successful!")
        return True
    
    driver.quit()

if __name__ == '__main__':
    success = login("s1234567","151")
    if success:
        print("Test passed - Login successful")
    else:
        print("Test failed - Could not login")
    

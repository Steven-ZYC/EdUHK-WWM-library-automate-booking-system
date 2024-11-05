import requests
import getpass
from bs4 import BeautifulSoup

url = 'https://app.lib.eduhk.hk/booking/admin.php'
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
data = {
    'NewUserName': '',  
    'NewUserPassword': ''
}

name = input("user name?(e.g s1234567)").lower()
data['NewUserName'] = name
data['NeaUserPassword'] =  getpass.getpass("Enter your password: (NOTE:YOUR PASSWORD WOULD NOT DISPLAY ON THE SCREEN)")

# Send the POST request
response = requests.post(url, data=data, headers=headers)


# Check if the request was successful
if response.status_code == 200:
    # Get the HTML response
    html_content = response.text
    print("Original HTML Response received:")
    print(html_content)

    # Parse the HTML with Beautiful Soup
    soup = BeautifulSoup(html_content, 'html.parser')

    free_seats = soup.findAll("div", atters={"class":"new"})
    my_yellow = soup.findAll("div",attrs={"class":"I tentative writable"})
    other_yellow = soup.findAll("div",attrs={"class":"I tentative"})
    other_red = soup.findAll("div",attrs={"class":"E"})
else:
    print(f"Error: {response.status_code}")




"""

my uncheckin book:     class="I tentative writable"
my checkin book:       class="E writable"
other uncheckin book:  class="I tentative" 
other checkedin book:  class="E"
can be book:           class="new"
"""

"""
app.lib.eduhk.hk/booking/checkin_entry.php?area=
"""
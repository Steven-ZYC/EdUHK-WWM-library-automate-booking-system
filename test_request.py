import requests
import getpass
from bs4 import BeautifulSoup

name = input("user name?(e.g s1234567)\n").lower()
passwd =  getpass.getpass("Enter your password: (NOTE:YOUR PASSWORD WOULD NOT DISPLAY ON THE SCREEN)\n")

#initialise the crawler. set a session for remain the login status
session = requests.Session()
url = 'https://app.lib.eduhk.hk/booking/admin.php'
headers = {"User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36 Edg/130.0.0.0"}
data = {
    'NewUserName': name,  
    'NewUserPassword': passwd
}
"""
<input type="text" id="NewUserName" name="NewUserName" value="" class="form-control">
<input type="password" id="NewUserPassword" name="NewUserPassword" class="form-control">
"""
# Send the POST request
response = session.post(url, json=data, headers=headers)


# Check if the request was successful
if response.status_code == 200:
    # Get the HTML response
    html_content = response.text
    print("Original HTML Response received:\n")
    #print(html_content)
    soup = BeautifulSoup(html_content, 'html.parser')
    form_tags = soup.findAll("form", attrs={"class":"navbar-brand"})
    # Ensure form_tag is not None 
    if form_tags: 
        login_detected = False 
        for form_tag in form_tags: 
            # Extract the text inside each form tag 
            form_text = form_tag.get_text(strip=True) 
            print(form_text) 
            if "Please loginLog in" in form_text: 
                login_detected = True 
        if login_detected: 
            print("Failed to log in. Please check your ID and password.") 
        else: 
            print("Login successful")
            free_seats = soup.findAll("div", attrs={"class":"new"})
            my_yellow = soup.findAll("div",attrs={"class":"I tentative writable"})
            other_yellow = soup.findAll("div",attrs={"class":"I tentative"})
            other_red = soup.findAll("div",attrs={"class":"E"})
            black = soup.findAll("div",attrs={"class":"S"})
    else: print('WARRNING! form_tag not found.\n The website of WWM library is updated.\n Pease post this issue to the "issues" column via github.\n')
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

    <ul class="dropdown-menu">
        <li><a href="day.php?area=1">4/F Research Commons</a></li>
        <li><a href="day.php?area=3">3/F Media Production Lab</a></li>
        <li><a href="day.php?area=5">3/F Language Learning Room</a></li>
        <li><a href="day.php?area=11">2/F STEM Room</a></li>
        <li><a href="day.php?area=7">1/F Discussion Zone & Creative Arts Room </a></li>
        <li><a href="day.php?area=43">1/F Discussion Booths</a></li>
        <li><a href="day.php?area=46">1/F Study Booths</a></li>
        <li><a href="day.php?area=6">G/F Quiet Zone &amp; PC Area</a></li>
        <li><a href="day.php?area=4">G/F Lounge</a></li>
        <li><a href="day.php?area=45">G/F Me Space</a></li>
        <li><a href="day.php?area=44">G/F Discussion Booths</a></li>
        <li><a href="day.php?area=10">LP/F EI Hub</a></li>
    </ul>
"""
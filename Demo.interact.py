import requests
from datetime import datetime
import webbrowser

current_time = datetime.now()
floor = {
    '4F zone A': 1, 
    '4F zone B': 2, 
    '3F Language Learning Room': 3,
    '3F Language Learning Room Duplicate': 5,  
    '2F Stem Room Markerspace': 11,
    '2F Stem Room workbench': 12,
    '1/F Discussion Zone Group Discussion Tables': 7,
    '1/F Discussion Zone Group Discussion Rooms': 8,
    '1/F Discussion Zone SEN Study Rooms/Faculty Reading Rooms': 9,
    '1/F Discussion Booths': 43,
    '1/F Study Booths': 46,
    '1/F Creative Arts Room': 41,
    'G/F Quiet Zone & PC Area': 6,
    'G/F Lounge': 4,
    'G/F Discussion Booths': 44,
    'LP/F EI Hub': 10
}
# floor[''] refer to area number from booking html

user_floor = input('''What is your floor number? Choose one:
4F zone A
4F zone B
3F Media Production Lab
3F Language Learning Room
2F Stem Room Markerspace
2F Stem Room workbench
1/F Discussion Zone Group Discussion Tables
1/F Discussion Zone Group Discussion Rooms
1/F Discussion Zone SEN Study Rooms/Faculty Reading Rooms
1/F Discussion Booths
1/F Study Booths
1/F Creative Arts Room
G/F Quiet Zone & PC Area
G/F Lounge
G/F Discussion Booths
LP/F EI Hub
''')
user_room_number = input('''what is your room number''')
user_room_time = input('''What is the time (hour) for using room:
9
11
13
15
17
19
21
''')
if user_floor in floor:
    area_number = floor[user_floor]
    url = f'https://app.lib.eduhk.hk/booking/edit_entry.php?area={area_number}&room=4&hour={user_room_time}&minute=30&year={current_time.year}&month={current_time.month}&day={current_time.day}'
    webbrowser.open(url)


from icalendar import Calendar, Event  
from datetime import datetime

cal = Calendar()

event = Event()
event.add('summary', 'Meeting with Bob')
event.add('dtstart', datetime(2024, 11, 20, 10, 0, 0))
event.add('dtend', datetime(2024, 11, 20, 11, 0, 0))
event.add('description', 'Discuss the project updates with Bob.')
event.add('location', 'Conference Room')

# 将事件添加到日历
cal.add_component(event)

# 将日历写入 .ics 文件
with open('meeting.ics', 'wb') as f:
  f.write(cal.to_ical())

# A brief user manual 

By ZHANG YANCHENG 

##  Table of Contents 
1. Introduction
2. Requirements and installation guide
3. Quick start

## 1. Introduction 


&#32;      First, I need to inform you, my dear professor, that this project is almost wrote by me,which means the disparity in contributions among our group members for the project "library seat booking system." You can refer to https://github.com/Steven-ZYC/EdUHK-WWM-library-automate-booking-system/graphs/contributors to check our group member's contribution, as we use GitHub to cooperate.

&#32;      I have studied git, session, cookies, request(a library of python), the difference of post and get in internet communication, selenium(another third party library of python),and  during the journey of solving this actual problem. 

### 1.1 Available Booking Areas
In this program, users can choose three areas to book seat 
&#32;   1. '4/F Research Commons A';
&#32;   2. '4/F Research Commons B';
&#32;   3. 'G/F Quiet Zone & PC Area'.

P.S. this program is dynamic, so only the seat which currently not in use or booked by others that can be booked.

### 1.2 Functions

&#32; My program used selenium library to connect EdUHK MMW library, and use "getpass" to protect students' account privacy

&#32; My program can technically book all available seat form three area in he library as I've mentioned,as due to the library's policy, you can only book one seat in one time slot. 

&#32; After users choose one seat, this program will automatically book whole day's available time slot of this seat.

### 1.3 Test case
&#32; According to my test, the run time of  program is about 1.5 mins(including user's input) 
 !screenshot:(<testcase of test_selenium(fully written by ZHANG YANCHENG)-1.png>)

## 2. Requirements and installation guide

### 2.1 Python environment
To use this program, you should first installed python in your computer. (Recommended edition of python：3.12.4 64-bit )

### 2.2  Third-party libraries installation guide
You need to download some third-party libraries for python as below.

```bash
pip install selenium
pip install argparase
```

## 3. Quick start

### 3.1 user name and password
&#32;users need to input their EdUHK id and password first
&#32;For reference:
&#32;Username:s1234567
&#32;Password123456789

### 3.2 Choose the area from the 3 choices

### 3.3 Choose the output mode from 2 mode

### 3.4 Choose the seat you want to book

### 3.5 Finished

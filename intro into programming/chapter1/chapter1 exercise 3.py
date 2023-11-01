#Exercise 3: Print Date and Time
#This execise is about showing the current date and time.
from datetime import datetime
now=datetime.now()

#
Date1=now.strftime("%m-%d-%Y %H:%M:%S")
print("Today’s Date and Time: ",Date1)
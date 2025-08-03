from datetime import datetime
from datetime import timedelta

d1 = datetime.now()
d2 = timedelta(hours= 23, minutes = 59, seconds = 59)
d3 = (d1-d2) 
print("{}:{}".format(d1.hour, d1.minute, d1.second),"time")

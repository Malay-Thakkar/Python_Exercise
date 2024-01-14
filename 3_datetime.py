# 2. Write a Python program to find out what version of Python you are using. 
# ample Output :
# Current date and time :
# 2014-07-05 14:34:14

import datetime
current_data = datetime.datetime.now() 
print("Current Date and time: " + current_data.strftime("%Y-%m-%d %H:%M:%S"))
from datetime import datetime
print("Current Date and Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

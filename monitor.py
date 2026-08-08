import socket
import getpass
from datetime import datetime

hostname = socket.gethostname()
current_user = getpass.getuser()
current_datetime = datetime.now()
print ("Hostname :" , hostname)
print ("Current User :" , current_user)
print ("Current Date & Time :", current_datetime) 

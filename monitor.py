import socket
import getpass
from datetime import datetime
import platform

hostname = socket.gethostname()
current_user = getpass.getuser()
current_datetime = datetime.now()
operating_system = platform.system()
kernal_version = platform.release()

print ("Hostname :" , hostname)
print ("Current User :" , current_user)
print ("Current Date & Time :", current_datetime) 
print ("Operating System :" , operating_system)
print ("Kernal Version :" , kernal_version)


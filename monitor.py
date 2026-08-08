import socket
import getpass
from datetime import datetime
import platform
import psutil

hostname = socket.gethostname()
current_user = getpass.getuser()
current_datetime = datetime.now()
operating_system = platform.system()
kernel_version = platform.release()
cpu_usage = psutil.cpu_percent(interval=1)

print ("Hostname :" , hostname)
print ("Current User :" , current_user)
print ("Current Date & Time :", current_datetime) 
print ("Operating System :" , operating_system)
print ("Kernel Version :" , kernel_version)
print ("CPU Usage :" ,cpu_usage, "%")

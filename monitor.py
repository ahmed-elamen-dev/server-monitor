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
memory = psutil.virtual_memory()
total_ram = memory.total / (1024 ** 3)
used_ram = memory.used / (1024 ** 3)
free_ram = memory.free / (1024 ** 3)
memory_usage = memory.percent

disk = psutil.disk_usage("/")

total_disk = disk.total / (1024 ** 3)
used_disk = disk.used / (1024 ** 3)
free_disk = disk.free / (1024 ** 3)
disk_usage = disk.percent

print ("Hostname :" , hostname)
print ("Current User :" , current_user)
print ("Current Date & Time :", current_datetime) 
print ("Operating System :" , operating_system)
print ("Kernel Version :" , kernel_version)
print ("CPU Usage :" ,cpu_usage, "%")
print("Memory Usage:")
print("Total :", round(total_ram, 2), "GB")
print("Used :", round(used_ram, 2), "GB")
print("Free :", round(free_ram, 2), "GB")
print("Usage :", memory_usage, "%")
print("Disk Usage:")
print("Total :", round(total_disk, 2), "GB")
print("Used :", round(used_disk, 2), "GB")
print("Free :", round(free_disk, 2), "GB")
print("Usage :", disk_usage, "%")

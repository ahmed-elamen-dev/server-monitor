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

network_interfaces = psutil.net_if_addrs()

ip_address = "N/A"

for interface, addresses in network_interfaces.items():
    for address in addresses:
        if address.family == socket.AF_INET and address.address != "127.0.0.1":
            ip_address = address.address
            break
    if ip_address != "N/A":
        break

boot_time = psutil.boot_time()
current_time = datetime.now().timestamp()

uptime_seconds = current_time - boot_time

days = int(uptime_seconds // 86400)
hours = int((uptime_seconds % 86400) // 3600)
minutes = int((uptime_seconds % 3600) // 60)


print ("Hostname :" , hostname)
print ("Current User :" , current_user)
print ("Current Date & Time :", current_datetime) 
print ("Operating System :" , operating_system)
print ("Kernel Version :" , kernel_version)
print ("CPU Usage :" ,cpu_usage, "%")
print ("Memory Usage:")
print ("Total :", round(total_ram, 2), "GB")
print ("Used :", round(used_ram, 2), "GB")
print ("Free :", round(free_ram, 2), "GB")
print ("Usage :", memory_usage, "%")
print ("Disk Usage:")
print ("Total :", round(total_disk, 2), "GB")
print ("Used :", round(used_disk, 2), "GB")
print ("Free :", round(free_disk, 2), "GB")
print ("Usage :", disk_usage, "%")
print ("Ip Address :" , ip_address)
print ("Uptime :", days, "days,", hours, "hours,", minutes, "minutes")

report = f"""==============================
SERVER HEALTH REPORT
==============================

Hostname : {hostname}
Current User : {current_user}
Date : {current_datetime}
Operating System : {operating_system}
Kernel : {kernel_version}

CPU Usage : {cpu_usage} %

Memory Usage:
Total : {total_ram:.2f} GB
Used : {used_ram:.2f} GB
Free : {free_ram:.2f} GB
Usage : {memory_usage} %

Disk Usage:
Total : {total_disk:.2f} GB
Used : {used_disk:.2f} GB
Free : {free_disk:.2f} GB
Usage : {disk_usage} %

IP Address : {ip_address}

Uptime : {days} Days, {hours} Hours, {minutes} Minutes
==============================
"""

with open("reports/server_report.txt", "w") as file:
    file.write(report)

print ("Report generated successfully: reports/server_report.txt")

import socket
import getpass
hostname = socket.gethostname()
current_user = getpass.getuser()

print ("Hostname :" , hostname)
print("Current user :" , current_user)

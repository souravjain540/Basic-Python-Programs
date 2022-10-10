# Github username: rajdeepdas2000
# Aim: print IP Address and Hostname
# Date: 04-10-2022

import socket
hostname=socket.gethostname()
hostIP=socket.gethostbyname(hostname)
print("Hostname: ",hostname)
print("IP Address: ",hostIP)
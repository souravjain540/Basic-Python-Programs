import sys
import pyfiglet
import socket
import datetime

# banner
banner = pyfiglet.figlet_format("Port scanner")
print(banner)
print("---Made by Pranav Sharma")

# take input from user as ip target
target_ip = input("Enter the ip: ")
rng= int(input("Enter the maximum port till which you want to scan: "))
# banner
print("*" * 50)
print("Scanning target " + target_ip)
print("Scanning start at " + str(datetime.datetime.now()))
print("*" * 50)

# port scanner
try:
    for port in range(1, rng):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        #         return open port
        r = s.connect_ex((target_ip, port))
        if r == 0:
            print(f"[#] Port {port} is open")
            s.close()
except KeyboardInterrupt:
    print("\n Exiting :(")
    sys.exit()
except socket.error:
    print("\ Host not responding :( ")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
    sys.exit()


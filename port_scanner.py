import pyfiglet
import sys
import socket
from datetime import datetime

banner = pyfiglet.figlet_format("PORT SCANNER")
print(banner)

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    sys.exit()

print("-" * 50)
print(f"Scanning Target: {target}\n")
print(f"Scanning Started at : {str(datetime.now())}\n")
print("-" * 50)

try:
    for port in range(1, 65535):
        print(f"Checking Port: {port}\n")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open\n")
        s.close()
except KeyboardInterrupt:
    print("Exiting")
    sys.exit()
except scoket.gaierror:
    print("Bad Host Name")
    sys.exit()
except socket.error:
    print("Server not responding")
    sys.exit()

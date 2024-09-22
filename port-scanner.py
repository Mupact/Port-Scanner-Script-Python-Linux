#Port Scanner for Python version 3.12. 

import socket 
import subprocess
import sys 
from datetime import datetime

#Blanks the screen.
subprocess.call('clear, shell=True')

#Ask for input.
remoteServer = input("Enter your remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

#Prints a banner with information on host to be scanned.
print("-" * 60)  # Prints a line of 60 dashes.
print(f"Scanning in progress for {remoteServerIP}")
print("-" * 60)  # Prints another line of 60 dashes.


#Verifies the date and time the scan began.
t1 = datetime.now()

#The range function specifies ports and handles error handling.
try: 
    for port in range (1,5000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = socket.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}:     Open".format(port))
        sock.close()
        
except KeyboardInterrupt:
        print("You pressed Ctrl+C, Scan ceasing")
        sys.exit()

except sock.gaierror:
     print("Hostname could not be resolved.")
     sys.exit()

#Verifying time again.
t2 = datetime.now()

#Scan progression difference timer
total = t2 - t1 

#Outputting information on the screen
print("Scan completed in: "), total 
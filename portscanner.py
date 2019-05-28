#!/usr/bin/enn python
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

def main():
#ask for input
    serv   = input("Please enter a host to scan: ")
    servIP = socket.gethostbyname(serv)

# print a banner with host info 
    print("-" * 60)
    print("PLease wait, scanning host...", servIP)
    print("-" * 60)

# check what time the scan started
    start = datetime.now()

# Using the range function to specify ports(between 1 and 1024)
    try:
        for port in range(1,1025):
            sockx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sockx.settimeout(0.5)
            res   = sockx.connect_ex((servIP, port)) 
            if res == 0:
                print("Port {}: Open".format(port))
            sockx.close()

# exceptions for error handling
    except KeyboardInterrupt:
        print("you pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()

    except socket.error:
        print("Couldn't connect to server") 
        sys.exit()

#check time again
    finish = datetime.now()

#find and print the difference from start to finish
    total = finish - start

    print("Scanning completed in: ", total)

main()

#run scanner again
while True:
    again = input("Would you like to scan another host? (y/n): ")
    if again not in ('y', 'n'):
        print("Not a valid input.")
        break
    if again == 'y':
        main()
    else:
        print("Goodbye ")
        break




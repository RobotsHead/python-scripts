#!/usr/bin/env python3
import urllib.request
import re


def main():
    url = "http://checkip.dyndns.org"
    print("Using {} to get my IP".format(url))
    request = urllib.request.urlopen(url).read().decode('utf-8')
    myip = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", request)
    print("My IP is: {}".format(myip))


main()

while True:
    again = input("Run again? (y/n): ")
    if again not in ('y', 'n'):
        print("Not a valid input.")
        break
    if again == 'y':
        main()
    else:
        break


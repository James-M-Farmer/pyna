#!/usr/bin/env python3

import netifaces

for m in netifaces.interfaces():
    print('\n****** details of interface - ' + m + ' ******')
    try:
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print((netifaces.ifaddresses(m)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message

for i in netifaces.interfaces():
    print('\n****** details of interface - ' + i + ' ******')
    try:
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message

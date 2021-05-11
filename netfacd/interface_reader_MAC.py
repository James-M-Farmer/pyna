#!/usr/bin/env python3
  
import netifaces

for i in netifaces.interfaces():
    print('\n****** details of interface - ' + i + ' ******')
    try:
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message

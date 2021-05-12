#!/usr/bin/env python3
  
import netifaces

def get_ip(interface):
    return (inetifaces.ifaddresses(interface)[netifaces.AF_INET])[0]['addr']

def get_mac(interface):
    return (inetifaces.ifaddresses(interface)[netifaces.AF_LINK])[0]['addr']

def main():
    print(netifaces.interfaces())
    for i in netifaces.interfaces():
        print('\n****** details of interface - ' + i + ' ******')
        try:
            print(f'MAC: {get_mac(i)}')
            print(f'IP: {get_ip(i)}') 
        except:          # This is a new line
            print('Could not collect adapter information') # Print an error message

if __name__ == "__main__":
    main()
    #pint(get_mac("docker0"))

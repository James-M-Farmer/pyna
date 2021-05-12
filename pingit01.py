#!/usr/bin/python3
import os
import argparse

## Ping router - returns True or False
def ping_router(hostname):

    response = os.system("ping -c 1 " + hostname)

    #and then check the response...
    if response == 0:
        return True
    else:
        return False

def main():
    switchlist = ["172.0.1.2", "sw-1", "sw-2" "8.8.8.8"]   # CUSTOMIZE THIS LIST WITH IPs to PING

    ## Use a loop to check each device for ICMP responses
    print("\n***** STARTING ICMP CHECKING *****")
    for {args.name} in switchlist:
        if ping_router({args.name}):
            print(f"IP address {x} is responding to ICMP")
        else:
            print(f"IP address {x} is not responding to ICMP")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IP")
    parser.add_argument("-ip", help="entire IP to ping")
    main()


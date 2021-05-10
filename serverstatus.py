#!/usr/bin/python3
"""opening a file for status of servers"""
  
import json

def main():
    """runtime code"""
    ## open the file
    with open("status.json", "r") as status:
        statusstring = status.read('down')
    
    ## display our decoded string
    print(statusstring)

    ## Create the JSON string
    statusdecoded = json.loads(statusstring)
    
    ## display the servers state
    print(statusdecoded("state"))
    
if __name__ == "__main__":
    main()


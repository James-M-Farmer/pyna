#!/usr/bin/python3
"""opening a file for status of servers"""
  
import json

with open("status.json", "r") as status:
    statusstring = json.load(status)
    print(statusstring)
    down=[]
    for serv in statusstring:
        if serv["state"] == "down":
            down.append(serv)

print(f"The following is a list of all the servers in a 'down' state: {down}")

with open ("downed_servers.txt", "w") as f2:
    spaced_servers = [f"{srv['server']}\n" for srv in down]
    f2.writelines(spaced_servers)


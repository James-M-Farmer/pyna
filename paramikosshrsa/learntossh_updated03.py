#!/usr/bin/env python3

import os
import paramiko
from jrprogrammer import cmdissue


def get_creds():
    ip = input("IP: ")
    user = input("Username: ")
    # return [ip, user]
    # return {"ip": ip, "user": user}
    return (ip, user)

def get_cmds() -> list:
    cmds = []
    while True:
        cmd = input("What command would you like to run?")
        cmds.append(cmd)
        return cmds

def main():
    sshsession = paramiko.SSHClient()
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

  ## create SSH connection
    while True:
        try:
            creds = get_creds()
            host = creds[0]
            user = creds[1]
            sshsession.connect(hostname=host, username=user, pkey=mykey)
        
            our_commands = get_cmds()
            for x in our_commands:
              resp = cmdissue(x, sshsession)
              if resp != "":
                print(resp)
        
            sshsession.close()
        except KeyboardInterrupt as err:
            print("Lunch time!!!")
            break

if __name__ == '__main__':
  main()


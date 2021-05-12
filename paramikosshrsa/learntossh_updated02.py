#!/usr/bin/env python3

import os
import paramiko
from jrprogrammer import cmdissue



def get_cmds() -> list:
    cmds = []
    while True:
        try:
            cmd = input("What command would you like to run? Press ctrl+c when done")
            cmds.append(cmd)
        except KeyboardInterrupt as err:
            print(err)
            break
    return cmds

def main():
  sshsession = paramiko.SSHClient()
  sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

  sshsession.connect(hostname='10.10.2.3', username='bender', pkey=mykey)

  our_commands = get_cmds()

  for x in our_commands:
    resp = cmdissue(x, sshsession)
    if resp != "":
      print(resp)

  sshsession.close()

if __name__ == '__main__':
  main()


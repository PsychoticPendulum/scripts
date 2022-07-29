#! /usr/bin/env python3

import os
import subprocess
from PyTerm import *
from time import sleep
from pythonping import ping


class NETWORK:
    hosts = []
    result = ''

def Update():
    NETWORK.result = ''
    for host in NETWORK.hosts:
        ip,name = host.split(',')
        buffer = ' ' * (os.get_terminal_size().columns - (len(name) + len(ip) + 12))
        NETWORK.result += f'{UTIL.BOLD}{name}{UTIL.RESET}@{ip}{buffer}{GetStatus(ip)}\n'

def Display():
    print(f'{UTIL.CLEAR}{UTIL.TOP}',end='')
    print(NETWORK.result)

def Routine():
    while True:
        try:
           Update() 
           Display() 
        except KeyboardInterrupt:
            quit()

def GetStatus(ip):
    result = str(ping(f'{ip}',count=1,timeout=0.5)).split('\n')[0]
    if 'timed' in result:
        return f'{UTIL.RESET}{FG.BLACK}{BG.RED}  Offline  {UTIL.RESET}'
    return f'{UTIL.RESET}{FG.BLACK}{BG.GREEN}  Online   {UTIL.RESET}'

def GetHosts():
    hosts = os.popen('cat /etc/hosts').read().split('# Local DNS')[1]
    hosts = hosts.split('\n')
    for host in hosts:
        if len(host):
            NETWORK.hosts.append(host.replace('\t',','))

if __name__ == '__main__':
    GetHosts()
    Routine()

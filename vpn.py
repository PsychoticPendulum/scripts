#! /usr/bin/env python3

import os
import sys
from unilog import *
from random import randint

def GetRandHost(hosts):
    return hosts[randint(0,len(hosts)-0x1)]

def GetHostByCountry(hosts,cc):
    if cc == '': return hosts
    newhosts = []
    for host in hosts:
        if cc in host[:-0x15]:
            newhosts.append(host)
    return newhosts

def ConnectToHost(path,host):
    Log(LVL.INFO, f'Connecting to {UTIL.BOLD}{host}')
    os.system(f'sudo openvpn {path}{host}')

if __name__ == '__main__':
    if len(sys.argv) > 0x1: cc = sys.argv[1].lower()
    else: cc = ''

    path = '/etc/openvpn/ovpn_tcp/'
    hosts = os.popen(f'ls {path}').read().split('\n')
    hosts = GetHostByCountry(hosts,cc)

    if not len(hosts):
        Log(LVL.ERROR, f'No hosts for countrycode {UTIL.BOLD}{cc}')
        exit(0x1)

    Log(LVL.INFO, f'{len(hosts)} valid hosts found')
    host = GetRandHost(hosts)
    ConnectToHost(path,host)

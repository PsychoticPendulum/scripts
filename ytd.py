#! /usr/bin/env python3

from Log import *
from sys import argv
from os import system

if __name__ == '__main__':
    if len(argv) < 2:
        exit(1)
    
    try:
        file = open(argv[1], 'r')
        for line in file.readlines():
            line = line.rstrip('\n')
            system(f'youtube-dl {line}')
        file.close()
    except PermissionError:
        Log(LVL.ERROR, f"Insufficient permissions to read: {UTIL.BOLD}{argv[1]}")                                      
    except FileNotFoundError:
        Log(LVL.ERROR, f"File does not exist: {UTIL.BOLD}{argv[1]}")  

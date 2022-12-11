#! /usr/bin/env python3

from sys import argv
from os import system
from time import sleep

if __name__ == "__main__":
    delay = 100
    if len(argv) > 1:
        delay = int(argv[1])
    while True:
        for i in range(256):
            system(f"pub binary {i}")
            sleep(float(delay)/1000)

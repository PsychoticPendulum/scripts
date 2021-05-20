#! /usr/bin/env python3
# |-------------------------------------------------------------------------|
# |  ____                 _     _      ____                        _        |
# | |  _ \ ___ _   _  ___| |__ (_) ___|  _ \ ___ _ __   __ _ _   _(_)_ __   |
# | | |_) / __| | | |/ __| '_ \| |/ __| |_) / _ \ '_ \ / _` | | | | | '_ \  |
# | |  __/\__ \ |_| | (__| | | | | (__|  __/  __/ | | | (_| | |_| | | | | | |
# | |_|   |___/\__, |\___|_| |_|_|\___|_|   \___|_| |_|\__, |\__,_|_|_| |_| |
# |           |___/                                   |___/                 |
# |-------------------------------------------------------------------------| 

import os

class Links:
    list = []
    amount = 0

def read_file():
    file = open("links.txt", "r+")
    for line in file.readlines():
        line = line.rstrip("\n")
        Links.list.append(line)
        Links.amount += 1

def download():
    for link in Links.list:
        print(link)

def main():
    read_file()
    download()

main()

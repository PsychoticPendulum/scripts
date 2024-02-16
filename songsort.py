#! /usr/bin/env python3

import os
import sys
from unilog import *

def CheckForValidity(entry):
    if len(entry.split(" - ")) == 2:
        return True
    return False

def ParseFile(fileptr):
    contents = []
    file = open(fileptr, "r")
    for line in file.readlines():
        if CheckForValidity(line):
            print(line.rstrip('\n'),end=" ; ")

if __name__ == "__main__":
    os.system("$EDITOR songs.tmp")
    ParseFile("songs.tmp")
    os.system("rm songs.tmp")

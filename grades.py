#! /usr/bin/env python3

import sys
from unilog import *

if __name__ == "__main__":
    if len(sys.argv) < 2:
        Log(LVL.ERROR, "Not enough arguments")
        exit(1)

    grades = []
    file = open(sys.argv[1],"r")
    for line in file.readlines():
        line = line.rstrip('\n')
        try:
            grades.append(int(line))
        except:
            pass

    total = 0
    for i in range(len(grades)):
        total += grades[i]
    print(f"{total} / {len(grades)+1} = {total/(len(grades)+1)}")

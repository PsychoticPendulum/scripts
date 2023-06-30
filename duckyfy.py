#! /usr/bin/env python3

import sys

file = open(sys.argv[1], "r")
for line in file.readlines():
    print(f"STRING {line}",end="ENTER\n")

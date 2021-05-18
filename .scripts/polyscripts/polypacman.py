#! /usr/bin/env python3

import os

PAC = os.popen("pacman -Q | wc -l").read()
PAC = PAC.strip("\n")
print("pacman: " + PAC)

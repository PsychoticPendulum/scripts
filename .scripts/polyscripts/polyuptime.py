#! /usr/bin/env python3

import os

ups = os.popen("uptime -s").read()
ups = ups.strip("\n")
upp = os.popen("uptime -p").read()
upp = upp.strip("\n")
print(upp)

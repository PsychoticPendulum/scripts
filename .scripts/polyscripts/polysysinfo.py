#!/usr/bin/env python3

import os

OS = os.popen("uname").read()
OS = OS.strip("\n")
VER = os.popen("uname -r").read()
VER = VER.strip("\n")
ARC = os.popen("uname --m").read()
ARC = ARC.strip("\n")
print("Artix " + OS + " " + VER + " " + ARC)

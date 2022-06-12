#! /usr/bin/env python3
# |-------------------------------------------------------------------------|
# |  ____                 _     _      ____                        _        |
# | |  _ \ ___ _   _  ___| |__ (_) ___|  _ \ ___ _ __   __ _ _   _(_)_ __   |
# | | |_) / __| | | |/ __| '_ \| |/ __| |_) / _ \ '_ \ / _` | | | | | '_ \  |
# | |  __/\__ \ |_| | (__| | | | | (__|  __/  __/ | | | (_| | |_| | | | | | |
# | |_|   |___/\__, |\___|_| |_|_|\___|_|   \___|_| |_|\__, |\__,_|_|_| |_| |
# |           |___/                                   |___/                 |
# |-------------------------------------------------------------------------| 

import random
import os

lines = []
total_lines = 0

file = open('/home/psychicpenguin/Developer/.scripts/assets/loaf.txt', 'r+')
for line in file.readlines():
	line = line.rstrip('\n')
	lines.append(line)
	total_lines += 1

choice = random.randint(0, total_lines)
if choice == total_lines:
    print("Drink some water, HydroHomie!")
else:
    print("[" + str(choice + 1) + "/" + str(total_lines) + "] " + lines[choice]) 

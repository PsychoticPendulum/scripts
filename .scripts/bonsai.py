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
import random

lines = []
total_lines = 0

file = open("/home/psychoticpendulum/Developer/.scripts/assets/loaf.txt", "r+")
for line in file.readlines():
    line = line.rstrip("\n")
    lines.append(line)
    total_lines += 1

choice = random.randint(0, total_lines - 1)
msg = "[" + str(choice + 1) + "/" + str(total_lines) + "] " + lines[choice]
seed = random.randint(0, 999983)
cmd = "cbonsai --seed " + str(seed) + " --live -m \"" + msg + "\""

os.system(cmd)

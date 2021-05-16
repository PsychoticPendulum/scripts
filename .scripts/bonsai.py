import os
import random

lines = []
total_lines = 0

file = open("/home/psychicpeanut/Developer/.scripts/assets/loaf.txt", "r+")
for line in file.readlines():
    line = line.rstrip("\n")
    lines.append(line)
    total_lines += 1

choice = random.randint(0, total_lines - 1)
msg = "[" + str(choice + 1) + "/" + str(total_lines) + "] " + lines[choice]
seed = random.randint(0, 999983)
cmd = "cbonsai --seed " + str(seed) + " --live -m \"" + msg + "\""

os.system(cmd)

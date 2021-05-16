import random
import os

lines = []
total_lines = 0

file = open('/home/psychicpeanut/Developer/.scripts/assets/loaf.txt', 'r+')
for line in file.readlines():
	line = line.rstrip('\n')
	lines.append(line)
	total_lines += 1

choice = random.randint(0, total_lines)
if choice == total_lines:
    os.system("python3 ~/Developer/.scripts/bonsai.py")
else:
    print("[" + str(choice + 1) + "/" + str(total_lines) + "] " + lines[choice] + "\n") 

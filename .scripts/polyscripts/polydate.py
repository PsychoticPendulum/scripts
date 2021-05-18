#!/usr/bin/env python3

import os
import math

out = os.popen('date +%s').read()
out = out.strip("\n")
out = str(math.sqrt(math.sqrt(int(out))))

print(out)

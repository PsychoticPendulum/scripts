#! /usr/bin/env python3

import sys
from pythonping import ping

if len(sys.argv) == 1:
    quit()

ping(f'{sys.argv[1]}',count=1,timeout=0.1,verbose=True)

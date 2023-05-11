#! /usr/bin/env python3

import os

if __name__ == "__main__":
    total = 0
    devs = os.popen("df | awk '{print $2}'").read().split('\n')
    for dev in devs:
        try:
            total += int(dev)
        except:
            pass
    print(f"{int(total/1024**2)}G")

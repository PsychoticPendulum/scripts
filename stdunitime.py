#! /usr/bin/env python3

import os
import sys
import select

def GetCurrentTime():
    result = os.popen("date +%s").read()
    result = result.rstrip("\n")
    return result

def ConvertTime(current, old):
    try:
        old = int(old)
        current = int(current)
    except:
        os.system("log ERROR 'Invalid Input'")
        return

    years   = 0
    days    = 0
    hours   = 0
    minutes = 0
    seconds = current - old
    if seconds < 0:
        os.system("log WARNING 'Input lies in the future'")
        seconds = abs(seconds)

    while seconds > 59:
        seconds -= 60
        minutes += 1
    while minutes > 59:
        minutes -= 60
        hours += 1
    while hours > 23:
        hours -= 24
        days += 1
    while days > 364:
        days -= 365
        years += 1

    result = str(years) + " years " + str(days) + " days " + str(hours) + " hours " + str(minutes) + " minutes " + str(seconds) + " seconds"
    print(result)

def main():
    if not select.select([sys.stdin, ], [], [], 0.0)[0]:
        os.system("log ERROR 'No input'")
        return

    for line in sys.stdin:
        ConvertTime(GetCurrentTime(), line)

if __name__ == "__main__":
    main()

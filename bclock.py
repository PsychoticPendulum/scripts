#! /usr/bin/env python3

import os
from datetime import datetime

def ToBinary(n):
    binary = ""
    while (n > 0):
        binary += str(n % 2)
        n = int(n / 2)
    return binary[::-1]

def ToSymbol(txt):
    result = ""
    for i in range(6 - len(txt)):
        result += ""
    for i in range(len(txt)):
        if txt[i] == "1":
            result += ""
        elif txt[i] == "0":
            result += ""
    return result

if __name__ == "__main__":
    now = datetime.now()
    h = now.strftime("%H")
    m = now.strftime("%M")
    s = now.strftime("%S")

    time = [0] * 3
    time[0] = ToSymbol(ToBinary(int(h)))
    time[1] = ToSymbol(ToBinary(int(m)))
    time[2] = ToSymbol(ToBinary(int(s)))

    print("", end="|")
    for i in range(3):
        print(time[i], end="|")

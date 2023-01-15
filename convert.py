#! /usr/bin/env python3

from PyTerm import *
from sys import argv

umlauts = ['ä','ö','ü','Ä','Ö','Ü','ß']
letters = ['\'',';','[','"',':','{','-']

def GetFile(file):
    try:
        return open(argv[1],'r')
    except FileNotFoundError:
        Log(LVL.ERROR, "File does not exist")
    except PermissionError:
        Log(LVL.ERROR, "Insufficient permissions to read file")
    exit(1)

def ParseFile(file):
    content = []
    for line in file.readlines():
       content.append(line)
    return content

def Replace(word):
    if len(word) == 1:
        return word
    for i in range(len(letters)):
        word = word.replace(letters[i],umlauts[i])
    return word

if __name__ == "__main__":
    if len(argv) < 2:
        Log(LVL.ERROR, "Not enough arguments")
        exit(1)

    content = ParseFile(GetFile(argv[1]))
    for sentence in content:
        for word in sentence.split(' '):
            print(Replace(word),end=' ')

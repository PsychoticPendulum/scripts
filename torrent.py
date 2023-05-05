#! /usr/bin/env python3

import os
import sys
from PyTerm import *

def ParseFile(fileptr):
    try:
        results = []
        file = open(fileptr, "r")
        for line in file.readlines():
            results.append(line.rstrip('\n'))
        file.close()
        return results
    except PermissionError:
        Log(LVL.ERROR, f"Insufficient permissions to read {fileptr}")
        exit(1)
    except FileNotFoundError:
        Log(LVL.ERROR, f"File does not exist: {fileptr}")
        exit(1)

def GetLink(name):
    name = name.replace("(","")
    name = name.replace(")","")
    name = name.replace(" ","+")
    
    try:    
        html = os.popen(f"curl -s 'https://1337x.to/search/{name}/1/' | grep '\[QxR\]'").read()
        html = (html.split("href=\"")[2]).split("\">")[0]
        html = f"https://1337x.to{html}"

        Log(LVL.INFO, f"Link Found!\n{UTIL.REVERSE}{html}")
        return html
    except:
        Log(LVL.ERROR, f"Unable to find {UTIL.REVERSE}{name}")
        return "ERROR"

def ExtractTorrent(link):
    torrent = os.popen(f"curl -s '{link}' | grep 'itorrents.org'").read()
    
    torrent = (torrent.split("href=\"")[1]).split("\">")[0]
    return torrent

def DownloadTorrent(torrent):
    os.system(f"wget -q '{torrent}'")

def GetTorrent(name):
    Log(LVL.INFO, f"Searching for {name}")
    link = GetLink(name)
    
    if link == "ERROR":
        os.system(f"echo '{name}' >> failed.txt")
        return  

    torrent = ExtractTorrent(link)
    print(torrent) 

    Log(LVL.INFO, "Downloading torrentfile ...")
    DownloadTorrent(torrent)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        Log(LVL.ERROR, "Not enough arguments")
        exit(1)
    
    Log(LVL.INFO, "Reading file ...")
    lines = ParseFile(sys.argv[1])
    for line in lines:
        GetTorrent(line)

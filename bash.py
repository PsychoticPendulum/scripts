#! /usr/bin/env python3

import os
import sys
import requests
from unilog import *

def GetJoke(html):
    html = html.split("class=\"quote\"")[1].split("<p")
    return html[0], html[1] 

def GetHTML(url):
    return requests.get(url).text

def FormatMeta(meta):
    meta = meta.split("class")
    iterate = meta[0]
    upvotes = meta[1]
    
    iterate = iterate.split("\"")[1].replace("?","")
    upvotes = upvotes.split("green\">")[1].split("</font")[0]
    
    print(f"{UTIL.BOLD}{FG.YELLOW}#{iterate}\t{FG.GREEN}{upvotes}{UTIL.RESET}")

def FixFormatting(text):
    fixes = [ "&lt;", "&quot", "&gt", ">", " class=\"qt\"", "</p" ]
    for fix in fixes:
        text = text.replace(fix,"")
    return text

def FormatJoke(joke):
    joke = joke.split("<br />")
    for line in joke:
        line = FixFormatting(line)
        line = line.split(";")
        print(f"{FG.CYAN}{line[0]}:{UTIL.RESET}{line[1]}",end="")

def Main():
    try:
        meta,joke = (GetJoke(GetHTML("http://bash.org/?random")))
        FormatMeta(meta)
        FormatJoke(joke)
        return 0
    except:
        return 1
    

if __name__ == "__main__":
    while Main():
        print(f"{UTIL.UP}{UTIL.CLEARLINE}",end="") 

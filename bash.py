#! /usr/bin/env python3

import os
import sys
import requests
from unilog import *

def GetJoke(html):
    return html.split("class=\"quote\"")[1].split("<p")

def GetHTML(url):
    return requests.get(url).text

def FormatJoke(joke):
    joke = joke.split("<br />")
    for line in joke:
        line = line.replace("&lt;","").replace("&quot","").replace("&gt","").replace(">","")
        line = line.split(";")
        print(f"{FG.GREEN}{line[0]}:{UTIL.RESET}{line[1]}",end="")

if __name__ == "__main__":
    try:
        joke,meta = (GetJoke(GetHTML("http://bash.org/?top")))
    except:
        Log(LVL.FAIL, "Something went wrong")

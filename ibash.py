#! /usr/bin/env python3

import os
import requests
from random import randint
from PyTerm import *

page_url = 'http://www.ibash.de/random.html'

def FormatLine(author, line):
    author = f'{UTIL.BOLD}{author}:'
    line = f'{UTIL.RESET}{line}'
    print(f'{author}\t{line}')

def PresentContent(content):
    for sentence in content:
        sentence = sentence.split('&gt;')
        FormatLine(sentence[0],sentence[1])

def WorkContent(content):
    content = content.split('<code>')
    del content[0]
    joke = []
    for i in range(len(content)):
        if '&gt' in content[i]:
            joke.append(content[i])

    result = []
    for line in joke:
        result.append(line.split('</code>')[0])

    PresentContent(result)

def GetContent():
    # Get HTML of page
    Log(LVL.INFO, 'Sending HTML request ...')
    content = requests.get(page_url).text

    # Only care about body
    Log(LVL.INFO, 'Removing head from body ...')
    content = content.split('<body>')
    content = content[1].split('class=quotetable')
    WorkContent(content[randint(1,20)]) 

if __name__ == '__main__':
    GetContent()

#! /usr/bin/env python3

import os
import requests
from random import randint
from PyTerm import *

class JOKE:
    pos     = ''
    date    = ''
    votes   = ''
    content = []

page_url = 'http://ibash.de/random.html'

def GetVoteColor(votes):
    if int(votes) > 0:
        return f'{FG.GREEN}'
    return f'{FG.RED}'

def FormatMessage(msg):
    author  = msg.split('&gt; ')[0]
    text    = msg.split('&gt; ')[1]
    buffer  = ' ' * (7 - len(author))
    print(f'{UTIL.RESET}{UTIL.BOLD}<{author}>\n{UTIL.RESET}{text}')

def PresentJoke(joke):
    # Present Metadata
    print(f'{UTIL.RESET}{UTIL.BOLD}{joke.pos}',end='\t')
    print(f'{UTIL.RESET}{joke.date}',end='\t')
    print(f'{UTIL.RESET}{GetVoteColor(joke.votes)}{joke.votes}',end='\t')
    print(f'{UTIL.RESET}')

    # Present Message
    for msg in joke.content:
        FormatMessage(msg)

def ParseQuote(html):
    # Initialize joke instance
    joke = JOKE()

    # Get joke metadata
    joke.pos    = html.split('zeige Zitat ')[1].split('"')[0]
    joke.date   = html.split('&nbsp;&nbsp;')[4].split('</td>')[0]
    joke.votes  = html.split('onclick=\'vote')[1].split(';')[0].split(',')[2][:-1]

    # Filter conversation    
    convo = html.split('code')
    for msg in convo:
        if '&gt;' in msg: joke.content.append(msg[1:][:-2])

    PresentJoke(joke)

def ibash():
    # Get raw html of page
    html = requests.get(page_url).text
    
    # Fix encoding
    html = html.replace('&szlig;','ß')
    html = html.replace('&auml;','ä')
    html = html.replace('&ouml;','ö')
    html = html.replace('&uuml;','ü')
    html = html.replace('&quot;','"')
    html = html.replace('&lt;','<')
    
    # Remove head from body
    html = html.split('body')
    html = html[1].split('class=quotetable')

    # Select random quote
    ParseQuote(html[randint(1,20)])

if __name__ == '__main__':
    ibash()

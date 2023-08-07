#! /usr/bin/env python3

import sys
import readline
from unilog import *


logo = [
    f"{FG.CYAN}",
    f"__   __      ____ _  ___  _     _ ",
    f"\ \ / /   _ / ___(_)/ _ \| |__ | |",
    f" \ V / | | | |  _| | | | | '_ \| |",
    f"  | || |_| | |_| | | |_| | | | |_|",
    f"  |_| \__,_|\____|_|\___/|_| |_(_)",
    f"{UTIL.RESET}"
]


class PlayerLost(Exception):
    pass


class Player:
    def __init__(self, index, name, lifepoints):
        self.index      = index
        self.name       = name
        self.lifepoints = lifepoints
    
    def Damage(self, points):
        self.lifepoints += points
        if self.lifepoints <= 0:
            raise PlayerLost(f"{FG.RED}{UTIL.REVERSE}{self.name} lost with {UTIL.BOLD}{self.lifepoints}{UTIL.RESET}")


def Display(players):
    for part in logo:
        print(part)

    for player in players:
        buffer = " " * (16 - len(player.name))
        print(f"{UTIL.BOLD}[{player.index}]{FG.GREEN} {player.name}:{buffer}{UTIL.RESET}{player.lifepoints}")


def Prompt(players):
    print(f"{UTIL.CLEAR}{UTIL.TOP}",end="")
    Display(players) 
    command = input(">> ").lower().split(" ")
    
    try:
        for player in players:
            if not str(player.index) == command[0]:
                continue
            player.Damage(int(command[1])) 
    except PlayerLost as e:
        print(e)
        exit()
    except:
        pass


if __name__ == "__main__":
    players = []

    for i in range(1,len(sys.argv)):
        players.append(Player(i, sys.argv[i], 8000))

    while True:
        try:
            Prompt(players)
        except KeyboardInterrupt:
            exit(0)

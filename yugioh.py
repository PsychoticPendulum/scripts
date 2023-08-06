#! /usr/bin/env python3

import sys
import readline
from unilog import *


class PlayerLost(Exception):
    pass


class Player:
    def __init__(self, name, lifepoints):
        self.name       = name
        self.lifepoints = lifepoints
    
    def Damage(self, points):
        self.lifepoints += points
        if self.lifepoints <= 0:
            raise PlayerLost(f"{self.name} lost")


def Display(players):
    for player in players:
        buffer = " " * (16 - len(player.name))
        print(f"{FG.GREEN}{UTIL.BOLD}{player.name}:{buffer}{UTIL.RESET}{player.lifepoints}")


def Prompt(players):
    print(f"{UTIL.CLEAR}{UTIL.TOP}",end="")
    Display(players) 
    command = input(">> ").lower().split(" ")
    
    try:
        for player in players:
            if not player.name.lower() == command[0]:
                continue
            player.Damage(int(command[1])) 
    except PlayerLost as e:
        print(e)
        exit()
    except:
        pass


if __name__ == "__main__":
    players = []

    for name in sys.argv[1:]:
        players.append(Player(name, 8000))

    while True:
        try:
            Prompt(players)
        except KeyboardInterrupt:
            exit(0)

#! /usr/bin/env python3

import os
from Log import *

def GetUser():
    return os.popen("echo $USER").read().rstrip("\n")

PATH = f"/home/{GetUser()}"
DEST = [
        "/mnt/media/backups/FullBackup/",
        "/mnt/NAS/backups/FullBackup"
]

FILES = [
    ".vimrc",
    ".bashrc"
]

DIRS = [
    "Developer",
    "Wallpapers",
    ".vim",
    ".stasi",
    ".screenlayout",
    ".school",
    ".log",
    ".info",
]

CFGS = [
    "fish",
    "i3",
    "kitty",
    "neofetch",
    "picom",
    "polybar",
    "ranger",
    "rofi",
    "xfce4",
]

def Backup(DEST):
    print("")
    Log(LVL.INFO, f"{UTIL.REVERSE}Sending backup to: {UTIL.UNDERLINE}{DEST}")
    if not os.path.exists(DEST):
        Log(LVL.ERROR, f"Path does not exist:\t{UTIL.UNDERLINE}{DEST}")
        return

    # Basic Files
    for FILE in FILES:
        Log(LVL.INFO, f"Backing up:\t{UTIL.UNDERLINE}{FILE}")
        os.system(f"rsync -rv {PATH}/{FILE} {DEST}")
    
    # Directories
    for DIR in DIRS:
        Log(LVL.INFO, f"Backing up:\t{UTIL.UNDERLINE}{DIR}")
        os.system(f"rsync -rv {PATH}/{DIR} {DEST}")

    # Configuration Files
    for CFG in CFGS:
        Log(LVL.INFO, f"Backing up:\t{UTIL.UNDERLINE}{CFG}")
        os.system(f"rsync -rv {PATH}/.config/{CFG} {DEST}/.config/")


if __name__ == "__main__":
    for dest in DEST:
        Backup(dest)

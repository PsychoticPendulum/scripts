#! /usr/bin/env python3

import os
from Log import *

def GetUser():
    return os.popen("echo $USER").read().rstrip("\n")

PATH = f"/home/{GetUser()}"
DEST = [
        "/mnt/media/backups/FullBackup/",
        "/mnt/NAS/backups/FullBackup/"
]

FILES = [
    ".vimrc",
    ".bashrc"
]

DIRS = [
    "Developer",
    "Wallpapers",
    "Files",
    ".vim",
    ".stasi",
    ".screenlayout",
    ".log",
    ".info",
    ".newsboat",
    ".keys",
    ".minecraft"
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
    "rclone",
    "xfce4",
]

def Backup(DEST):
    print("")
    Log(LVL.INFO, f"{UTIL.REVERSE}Sending backup to: {UTIL.UNDERLINE}{DEST}")
    if not os.path.exists(DEST):
        Log(LVL.ERROR, f"Path does not exist:\t{UTIL.UNDERLINE}{DEST}")
        return

    # Capturing date
    os.system(f'date >> {DEST}backup.log')

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


def GetTime():
    return int(os.popen("date +%s").read().rstrip("\n"))

def GetDuration(start,end):
    seconds = end - start
    minutes = 0
    hours = 0
    while seconds > 59:
        minutes += 1
        seconds -= 60
    while minutes > 59:
        hours += 1
        minutes -= 60
    return f"{hours}h {minutes}m {seconds}s"

if __name__ == "__main__":
    start = GetTime()
    for dest in DEST:
        Backup(dest)
    end = GetTime()
    duration = GetDuration(start,end)
    Log(LVL.INFO, f"Total Time: {duration}")

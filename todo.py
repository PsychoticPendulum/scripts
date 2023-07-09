#! /usr/bin/env python3

import os
import sys
import json
import readline
from unilog import *

logo = [
    f" _____ ___  ____   ___  ",
    f"|_   _/ _ \|  _ \ / _ \ ",
    f"  | || | | | | | | | | |",
    f"  | || |_| | |_| | |_| |",
    f"  |_| \___/|____/ \___/   {FG.MAGENTA}by luks",
    f""
]

todo = {
    "demo task": False
}

list_file = "todo.json"

def ListEntries():
    PrintLogo()
    index = 1
    for task, status in todo.items():
        color = FG.GREEN if status else FG.RED
        print(f"[{index}]\t{color}{task}{UTIL.RESET}")
        index += 1


def AddEntry(cmd):
    entry = " ".join(cmd.split(" ")[1:])
    if entry == "":
        Log(LVL.WARN, "No task defined")
        return
    todo[entry] = False


def RemoveEntry(cmd):
    try:
        entry = cmd.split(" ")[1]
        entry = int(entry)
        if len(todo) < entry: raise 
    except:
        Log(LVL.WARN, f"Unknown task: {UTIL.UNDERLINE}{entry}")
        return
    
    index = 1
    for task, status in todo.items():
        if index == entry:
            entry = task
            break
        index += 1

    todo.pop(entry)
    

def CheckEntry(cmd):
    try:
        entry = cmd.split(" ")[1]
        entry = int(entry)
        if len(todo) < entry: raise 
    except:
        Log(LVL.WARN, f"Unknown task: {UTIL.UNDERLINE}{cmd}")
        return

    index = 1
    for task, status in todo.items():
        if index == entry:
            print(f"{task}, {status}, {index}, {entry}")
            todo[task] = False if status else True
            break
        index += 1


def Exit():
    SaveTasks()
    print(f"{UTIL.CLEAR}{UTIL.TOP}",end="")
    exit(0)


def SaveTasks():
    global list_file
    with open(list_file, "w") as json_file:
        json.dump(todo, json_file)


def LoadTasks(file):
    global todo
    global list_file
    if not os.path.exists(file):
        Log(LVL.WARN, "File not found")
        return

    with open(file, "r") as json_file:
        todo = json.load(json_file)


def PrintLogo():
    for line in logo:
        print(f"{FG.CYAN}{line}{UTIL.RESET}")


def Usage():
    print(f"Usage: todo.py [file]")
    print(f"")
    print(f"{UTIL.BOLD}Description:{UTIL.RESET}")
    print(f"    Simple tool to manage todo lists")
    print(f"")
    print(f"{UTIL.BOLD}Commands:{UTIL.RESET}")
    print(f"    help                show this menu")
    print(f"    exit                closed the program")
    print(f"    add <task>          add a new task")
    print(f"    remove [n]          remove task n")
    print(f"    check [n]           change state of task n")
    print("")


def Prompt():
    cmd = input(">> ")
    match cmd.split(" ")[0]:
        case "help":
            print(f"{UTIL.CLEAR}{UTIL.TOP}",end="")
            Usage()
            input("Press any key to continue ...")
        case "exit":
            Exit()
        case "add":
            AddEntry(cmd)
        case "remove":
            RemoveEntry(cmd)
        case "check":
            CheckEntry(cmd)
        case _:             
            Log(LVL.WARN, f"Unknown Command: {UTIL.UNDERLINE}{cmd}")
    print(f"{UTIL.CLEAR}{UTIL.TOP}",end="")
    ListEntries()


def main(argv):
    global list_file
    if len(argv):
        if argv[0] == "--help":
            Usage()
            exit()
        list_file = argv[0]
    LoadTasks(list_file)
    print(f"{UTIL.CLEAR}{UTIL.TOP}",end="")
    ListEntries()

    while True:
        try:
            Prompt()
        except KeyboardInterrupt:
            Log(LVL.WARN, f"Quitting due to keyboard interrupt")
            exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])

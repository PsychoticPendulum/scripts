#! /usr/bin/env python3

import os
import sys
from unilog import *
LOG.writeToFile = False

package_manager = ""


def DetectOS():
    supported_operating_systems = [
        "linux"
    ]

    if not sys.platform in supported_operating_systems:
        Log(LVL.FAIL, f"Operating System {UTIL.UNDERLINE}{sys.platform}{UTIL.RESET} is {FG.RED}not supported{UTIL.RESET}")

    Log(LVL.INFO, f"Operating System {UTIL.UNDERLINE}{sys.platform}{UTIL.RESET} is {FG.GREEN}supported{UTIL.RESET}")
    return sys.platform


def DetectDistro():
    supported_package_managers = [
        "yay", "pacman", "xbps-install", "apt", "dnf"
    ]
    
    for package_manager in supported_package_managers:
        if os.path.isfile(f"/usr/bin/{package_manager}"):
            Log(LVL.INFO, f"Package Manager detected: {FG.YELLOW}{package_manager}{UTIL.RESET}")
            return package_manager

    Log(LVL.FAIL, "No supported package manager found.")


def UniversalPackageManager(package_manager, action, arguments):
    match package_manager:
        case "yay":
            match action:
                case "update":
                    os.system("yay -Syyu")
                case "search":
                    os.system(f"yay -Ss {arguments}")
                case "install":
                    os.system(f"yay -S {arguments}")
                case "remove":
                    os.system(f"yay -Rs {arguments}")
        case "pacman":
            match action:
                case "update":
                    os.system("sudo pacman -Syyu")
                case "search":
                    os.system(f"sudo pacman -Ss {arguments}")
                case "install":
                    os.system(f"sudo pacman -S {arguments}")
                case "remove":
                    os.system(f"sudo pacman -Rs {arguments}")
        case "xbps-install":
            match action:
                case "update":
                    os.system("sudo xbps-install -Syu")
                case "search":
                    os.system(f"sudo xbps-query -Rs {arguments}")
                case "install":
                    os.system(f"sudo xbps-install {arguments}")
                case "remove":
                    os.system(f"sudo xbps-remove -R {arguments}")
        case "apt":
            match action:
                case "update":
                    os.system("sudo apt update && sudo apt upgrade")
                case "search":
                    os.system(f"sudo apt search {arguments}")
                case "install":
                    os.system(f"sudo apt install {arguments}")
                case "remove":
                    os.system(f"sudo apt remove {arguments}")
        case "dnf":
            match action:
                case "update":
                    os.system("sudo dnf update")
                case "search":
                    os.system(f"sudo dnf search {arguments}")
                case "install":
                    os.system(f"sudo dnf install {arguments}")
                case "remove":
                    os.system(f"sudo dnf remove {arguents}")
                
                

    Log(LVL.INFO, "Done")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        Log(LVL.FAIL, f"Not enough arguments.\n\tTry running {UTIL.BOLD}upm --help{UTIL.RESET}")

    action      = sys.argv[1]
    arguments   = ""
    for i in range(2,len(sys.argv)):
        arguments += f"{sys.argv[i]} "

    operating_system = DetectOS()
    package_manager  = DetectDistro()

    UniversalPackageManager(package_manager, action, arguments)

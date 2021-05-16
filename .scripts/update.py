import os

answer = str(input("Do you want to check for updates? [Y/n] "))
if answer == "yes" or answer == "Yes" or answer == "Y" or answer == "y":
    os.system("sudo pacman -Syu")

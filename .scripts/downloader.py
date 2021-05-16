import os

class Links:
    list = []
    amount = 0

def read_file():
    file = open("links.txt", "r+")
    for line in file.readlines():
        line = line.rstrip("\n")
        Links.list.append(line)
        Links.amount += 1

def download():
    for link in Links.list:
        print(link)

def main():
    read_file()
    download()

main()

#! /usr/bin/env python3

import os
import sys
from unilog import *

def GetDirectories(root):
    return [f.path for f in os.scandir(root) if f.is_dir()]

def IsGitRepo(directory):
    return os.path.isdir(f"{directory}/.git")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(1)
    root = sys.argv[1:]

    
    for subfolder in root:
        directories = GetDirectories(subfolder)
        for directory in directories:
            if IsGitRepo(directory):
                Log(LVL.INFO, f"{directory}")
                os.system(f"cd {directory}; git remote update; git pull; cd")

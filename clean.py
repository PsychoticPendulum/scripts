#! /usr/bin/env python3

import os

user = os.popen('whoami').read().rstrip('\n')

def DiskUsage():
    return os.popen('df / | awk \'{print $3}\' | tail -n 1').read().rstrip('\n')

def Clean():
    os.system(f'rm -Rfv /home/{user}/.cache/thumbnails')
    os.system(f'rm -Rfv /home/{user}/.cache/ranger')
    os.system(f'paccache -r')
    os.system(f'rm -Rfv /home/{user}/.cache/yay/*')
    os.system(f'rm -Rfv /var/cache/pacman/pkg/*')

if __name__ == '__main__':
    before = DiskUsage()
    Clean()
    after = DiskUsage()
    saved = (float(before) - float(after)) / 1000.0  
    print(f'Cleaned up {saved} MiB')

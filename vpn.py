import os
import random

class VPN_CONNECT:
    host_list = []
    hosts = 0
    location = ""
    ping_cmd = "ping -c 1 "

def create_hostfile():
    print("Looking for hostlist ...")
    if not os.path.isfile('/home/psychicpeanut/Developer/.scripts/assets/hostlist.txt'):
        print("No hostlist found. Creating new one ...")
        os.system("ls /etc/openvpn/ovpn_tcp >> /home/psychichpeanut/Developer/.scripts/assets/hostlist.txt")

def getLocation():
    VPN_CONNECT.location = str(input("Enter Country Code:\t"))

def read_hostlist():
    hostlist = open("/home/psychicpeanut/Developer/.scripts/assets/hostlist.txt", "r+")
    for line in hostlist.readlines():
        line = line.rstrip("\n")
        if VPN_CONNECT.location in line:
            VPN_CONNECT.host_list.append(line)
            VPN_CONNECT.hosts += 1

def establish_connection():
    looping = True
    while looping:
        os.system("clear")
        print(str(VPN_CONNECT.hosts) + " servers found.")
        choice = random.randint(0, VPN_CONNECT.hosts - 1)

        host = open("/etc/openvpn/ovpn_tcp/" + str(VPN_CONNECT.host_list[choice]))
        for line in host.readlines():
            if "remote " in line:
                count = 0
                for word in line.split():
                    if count == 1:
                        VPN_CONNECT.ping_cmd = "ping -c 1 "
                        VPN_CONNECT.ping_cmd += word
                    count += 1

        os.system(VPN_CONNECT.ping_cmd)
        print("\nConnecting to: " + str(VPN_CONNECT.host_list[choice]) + " ...")
        
        ui = str(input("Do you want to connect to this server? [Y/n]\t"))
        if ui == "Y" or ui == "y":
            print("\n\n")
            looping = False
            os.system("openvpn /etc/openvpn/ovpn_tcp/" + str(VPN_CONNECT.host_list[choice]))
        elif ui == "N" or ui == "n":
            print("\n")
            looping = False
            print("Exiting ...")

def main():
    create_hostfile()
    getLocation()
    read_hostlist()
    establish_connection()

main()

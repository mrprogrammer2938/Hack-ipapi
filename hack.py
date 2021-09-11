#!/usr/bin/python3
# This code write by Mr.nope
import os
import time
import sys
import subprocess
import platform

try: ## Try import ipapi and requests. If can't import a message show in the screen with command to install
   import ipapi
   import requests
except ImportError:
    print("Installing requirements...")
    os.system("pip install -r requirements.txt")

## Variables
opt = "\nHack/> "
ip = "\nEnter host: "


def cls(): ## Check the system operative to clean the output in terminal
    if platform.system == "Windows":
        os.system("cls")
    else:
        os.system("clear")

class color: ## Class to colors in terminal
     org = '\033[33m'
     End = '\033[0m'

def main(): ## Function main of the script
    cls()
    print("--------[ Hack-Ipapi ]--------\n")
    print("Version: 1.2.0\n")
    print("{1}.Port Scan")
    print("{2}.PingTest")
    print("{3}.Server Location")
    print("{4}.whois")
    print("{5}.Geoip")
    print("{99}.Exit")
    choose = input(opt)
    if choose == '1':
      portscan()
    elif choose == '2':
        pingtest()
    elif choose == '3':
        location()
    elif choose == '4':
        whois()
    elif choose == '5':
        geoip()
    elif choose == '99':
        cls()
        print("\nExiting...") 
    else:
        main()


def portscan(): ## Function to port scan IP Address
    cls()
    host = input(ip)
    attack_1 = requests.get(f"https://api.hackertarget.com/nmap/?q={host}").text
    print(attack_1)
    try1()

def try1(): ## You Choose if want attack again in portscan function
    try_to_portscan = input("\nDo you want to try again? [y/n] ").lower()
    if try_to_portscan == 'y':
      portscan()
    elif try_to_portscan == 'n':
        main()
    else:
        try1()

def pingtest(): ## Function to ping test IP Address
    cls()
    host = input(ip)
    packet = input("\nEnter packet: ")
    attack_2 = subprocess.getoutput(f"ping -w {packet} {host}")
    print(color.org + attack_2 + color.End)
    try2()

def try2(): ## You Choose if want attack again in pingtest function
    try_to_pingtest = input("\nDo you want to try again? [y/n] ").lower()
    if try_to_pingtest == 'y':
      pingtest()
    elif try_to_pingtest == 'n':
        main()
    else:
         try2()


def location(): ## Function to get location of IP Address
    cls()
    host = input(ip)
    search = ipapi.location(ip=host,key=None)
    print("------------------------\n")
    print("Ip: " + search["ip"])
    print("org: " + search["org"])
    print("------------------------\n")
    try3()

def try3(): ## You Choose if want get info in location function
    try_to_location = input("\nDo you want to try again? [y/n] ").lower()
    if try_to_location == 'y':
      location()
    elif try_to_location == 'n':
        main()
    else:
         try3()

def whois(): ## Function to info of IP Address
    cls()
    host = input(ip)
    attack_4 = requests.get(f"https://api.hackertarget.com/whois/?q={host}").text
    print(attack_4)
    try4()


def try4(): ## You Choose if want get info again in whois function
    try_to_whois = input("\nDo you want try again? [y/n] ").lower()
    if try_to_whois == 'y':
      whois()
    elif try_to_whois == 'n':
        main()
    else:
        try4()

def geoip(): ## Function to get GEO of IP Address
    cls()
    host = input(ip)
    attack_5 = requests.get(f"https://api.hackertarget.com/geoip/?q={host}").text
    print(attack_5)
    try5()

def try5(): ## You Choose if want get info again in geoip function
    try_to_geoip = input("\nDo you want to try again? [y/n] ").lower()
    if try_to_geoip == 'y':
      geoip()
    elif try_to_geoip == 'n':
        main()
    else:
        try5()


if __name__ == '__main__': ## To prevent importing into other scripts

    '''
    This way we can prevent it from being used in other scripts.
    This conditional is to run under special conditions.
    '''
    try:
        main()
    except KeyboardInterrupt: ## If user cancel operation this code is executed
         print("\nCtrl + C")
         print("\nExiting...")
         sys.exit()

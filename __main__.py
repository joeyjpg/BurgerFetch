#!/bin/python

from rich import print
import psutil
import time
import os
import psutil
import getpass
import socket

"""Do some config file checking"""
conf_path = os.path.expanduser('~/.config/burgerfetch/config.conf')
if os.path.isfile(conf_path):
    pass
else:
    print("[bold yellow]WARNING[/bold yellow]: Config file not found, attempting to copy default config.")
    exitstat = os.system("cp ./defaultconf.conf ~/.config/burgerfetch/config.conf > /dev/null 2>&1")
    if exitstat != 0:
        print("[bold red]FATAL ERROR[/bold red][white]: Config file is directory, Or default config file not found (or is also directory)")
        exit()
    else:
        print("[bold blue]INFO[/bold blue]: Successfully copied default config!")

"""Read the config file"""
try:
    with open(conf_path, 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    #print(lines)
    for i in lines:
        if "oslabel" in i:
            oslabel = i.replace("oslabel ", "")
        if "sysos " in i:
            #print("e")
            sysos = i.replace("sysos ", "")
        if "uplabel" in i:
            uplabel = i.replace("uplabel ", "")
        if "memlabel" in i:
            memlabel = i.replace("memlabel ", "")
    try:
        sysos
        oslabel
        uplabel
        memlabel
    except:
        print("[bold red]FATAL ERROR[/bold red]: You are missing the following from your configuration file:")
        try:
            sysos
        except:
            print("sysos")
        try:
            oslabel
        except:
            print("oslabel")
        try:
            uplabel
        except:
            print("uplabel")
        try:
            memlabel
        except:
            print("memlabel")
        print("Please fix the configuration file.")
except:
    print("[bold red]FATAL ERROR[/bold red]: I'm honestly not even sure what to write here. You passed all the config checks, yet burgerfetch can't open the config file? HOW?!")
    exit()

"""Get the system uptime"""
try:
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    hours = int(uptime_seconds // 3600)
    minutes = int((uptime_seconds % 3600) // 60)
    seconds = int(uptime_seconds % 60)
    endstr = []
    if hours >= 1:
        endstr.append(f"{hours}H")
    if minutes >= 1:
        endstr.append(f"{minutes}M")
    endstr.append(f"{seconds}S")
    sysuptime = " ".join(endstr)
except:
    print("[bold red]FATAL ERROR[/bold red]: Failed to get system uptime, somehow. Might be a good idea to check if your system is even functional?")
    exit()

"""Get some RAM information"""
total_memory = psutil.virtual_memory().total
used_memory = psutil.virtual_memory().used
totmem = round(total_memory / (1024 * 1024))
usemem = round(used_memory / (1024 * 1024))

"""Get the hostname and username"""
usernm = getpass.getuser()
hostnm = socket.gethostname()
hostnm = hostnm.replace("freaky", "𝓯𝓻𝓮𝓪𝓴𝔂")

os.system("clear")

print(f"[bold purple]{usernm}[/bold purple][bold white]@[/bold white][bold purple]{hostnm}[/bold purple] 🍔")
#print()
print(f"    [bold purple]{oslabel}[/bold purple]: {sysos}")
print(f"    [bold purple]{uplabel}[/bold purple]: {sysuptime}")
print(f"    [bold purple]{memlabel}[/bold purple]: [bold white]{usemem}[/bold white] MB / [bold white]{totmem}[/bold white] MB")
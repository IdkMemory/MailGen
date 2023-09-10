import requests
import asyncio
import shutil
import os
import pyfiglet
import time
from colorama import Fore, Style

class TextStyler:
    @staticmethod
    def warning(text):
        styled_text = f"{Fore.LIGHTYELLOW_EX}[!]{Fore.RESET}{Style.DIM} {text}{Fore.RESET}{Style.NORMAL}"
        return styled_text

    @staticmethod
    def success(text):
        styled_text = f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET}{Style.BRIGHT} {text}{Fore.RESET}{Style.NORMAL}"
        return styled_text

    @staticmethod
    def ask(text):
        styled_text = f"{Fore.LIGHTCYAN_EX}[?]{Fore.RESET}{Style.DIM} {text}{Fore.RESET}{Style.NORMAL}"
        return styled_text


def main(amount: int, write_to):
  print(TextStyler.success(f"Generating {amount} emails!\n"))
  url = f"https://www.1secmail.com/api/v1/?action=genRandomMailbox&count={amount}"
  r = requests.get(url)
  emailss = r.json()
  for email in emailss:
    if write_to =="y":
      with open("emails.txt", "a") as f:
        f.write(email + "\n")
    print(TextStyler.success(email))
  check()
    
def check():
    email = input(TextStyler.ask("What email address do you want to check the inbox of? \n"))
    login, domain = email.split('@')
    url2 = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
    r = requests.get(url2)
    emails = r.json()
    emailscount = 0
    for inbox in emails:
      emailscount += 1
    if emailscount == 0:
      print(TextStyler.warning("Inbox is empty!"))
    else:
      for x in r.json():
        id = x["id"]
      url3 = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={id}"
      r = requests.get(url3)
      print(TextStyler.success(r.json()["textBody"]))
    check()


text= """
 ██▒   █▓▓█████ ▒██   ██▒▒██   ██▒ ██▓   ▓██   ██▓
▓██░   █▒▓█   ▀ ▒▒ █ █ ▒░▒▒ █ █ ▒░▓██▒    ▒██  ██▒
 ▓██  █▒░▒███   ░░  █   ░░░  █   ░▒██░     ▒██ ██░
  ▒██ █░░▒▓█  ▄  ░ █ █ ▒  ░ █ █ ▒ ▒██░     ░ ▐██▓░
   ▒▀█░  ░▒████▒▒██▒ ▒██▒▒██▒ ▒██▒░██████▒ ░ ██▒▓░
   ░ ▐░  ░░ ▒░ ░▒▒ ░ ░▓ ░▒▒ ░ ░▓ ░░ ▒░▓  ░  ██▒▒▒ 
   ░ ░░   ░ ░  ░░░   ░▒ ░░░   ░▒ ░░ ░ ▒  ░▓██ ░▒░ 
     ░░     ░    ░    ░   ░    ░    ░ ░   ▒ ▒ ░░  
      ░     ░  ░ ░    ░   ░    ░      ░  ░░ ░     
     ░                                    ░ ░     
"""
text2 = f""" {Style.BRIGHT}{Fore.LIGHTBLUE_EX}███▄ ▄███▓ ▄▄▄       ██▓ ██▓      ▄████ ▓█████  ███▄    █ 
▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒     ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░    ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░    ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒░▒▓███▀▒░▒████▒▒██░   ▓██░
░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░ ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░  ░   ░  ░ ░  ░░ ░░   ░ ▒░
░      ░     ░   ▒    ▒ ░  ░ ░   ░ ░   ░    ░      ░   ░ ░ 
       ░         ░  ░ ░      ░  ░      ░    ░  ░         ░ 
                                                           
                                                    """




print(text.center(shutil.get_terminal_size().columns))

time.sleep(5)
os.system('cls' if os.name == 'nt' else 'clear')

print(text2)
print(TextStyler.warning("https://github.com/VexxlyCoding\n"))
amount = input(TextStyler.ask(f"How many emails to generate? \n"))

write_to = input(TextStyler.ask("Should we write the emails to a file? (y/n) \n"))
amount = int(amount)
main(amount, write_to)


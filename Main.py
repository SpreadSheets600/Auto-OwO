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

hunt_count = 0
battle_count = 0
pray_count = 0
gamble_count = 0
gamble_profit = 0
cookie_count = 0
cash_amt = 0
sell_count = 0
sell_profit = 0
inv_count = 0
rand_count = 0


async def hunt(channel):
    await channel.send("owo hunt")
    print(f"[ USED    ] ---- Hunt")
    hunt_count += 1

    webhook = DiscordWebhook(
            url=WEBHOOK_URL, content="```[ USED    ] ---- Hunt```"
        )

    webhook.execute()

    await asyncio.sleep(7)


async def battle(channel):
    await channel.send("owo battle")
    print(f"[ USED    ] ---- Battle")
    battle_count += 1

    webhook = DiscordWebhook(
            url=WEBHOOK_URL, content="```[ USED    ] ---- Battle```"
        )
    
    webhook.execute()

    await asyncio.sleep(7)

async def gamble(channel):

    randamt = random.randint(1,1000)

    await channel.send(f"owo flip {randamt}")
    print(f"[ USED    ] ---- Flip --- {randamt}")
    gamble_count += 1

    def check(m):
        return m.author != client.user and "sold" in m.content  
    
    gamble_message = await client.wait_for("message", check=check)

    if "spent" in gamble_message.content:

        content_split = gamble_message.content.split(' ')

        if "lost" in content_split[0]:
            gamble_profit = int(content_split[-1].split()[0])
            gamble_profit = gamble_profit * -1

            webhook = DiscordWebhook(
            url=WEBHOOK_URL, content="```[ USED    ] ---- Gamble\n[ LOST  ] ---- " + str(gamble_profit) + "```"

        )
    
            webhook.execute()

        elif "won" in content_split[0]:
            gamble_profit = int(content_split[-1].split()[0])

            webhook = DiscordWebhook(
            url=WEBHOOK_URL, content="```[ USED    ] ---- Gamble\n[ WON  ] ---- " + str(gamble_profit) + "```"

        )
    
            webhook.execute()

    await asyncio.sleep(7)

async def pray(channel):
    await channel.send("owo pray")
    print(f"[ USED    ] ---- Pray")
    pray_count += 1

    webhook = DiscordWebhook(
            url=WEBHOOK_URL, content="```[ USED    ] ---- Pray```"
        )
    
    webhook.execute()

    await asyncio.sleep(7)


async def rand_message(channel):
    random_owo_messages = ["owo", "uwu", "cute owo", "owo sexy", "owo love ya"]
    random_owo_faces = ["(・`ω´・)", ";;w;;", "owo", "UwU", ">w<", "^w^"]
    random_owo_actions = ["*nuzzles u*", "*winks*", "*notices bulge*"]

    await channel.send(
        random_owo_messages[random.randint(0, len(random_owo_messages) - 1)]
    )
    await channel.send(
        random_owo_faces[random.randint(0, len(random_owo_faces) - 1)]
    )
    await channel.send(
        random_owo_actions[random.randint(0, len(random_owo_actions) - 1)]
    )

    print(f"[ USED    ] ---- Random Message")
    rand_count += 1

    webhook = DiscordWebhook(
            url=WEBHOOK_URL, content="```[ USED    ] ---- Random Message```"
        )
    
    webhook.execute()


    await asyncio.sleep(7)


types = ["c", "r"]  # Chnage Type Accordingly


async def cookie(channel):
    global OWNER_ID

    await channel.send(f"owo cookie <@{OWNER_ID}>")
    print(f"[ GAVE    ] ---- Cookie")
    cookie_count += 1

    webhook = DiscordWebhook(
            url=WEBHOOK_URL, content="```[ GAVE    ] ---- Cookie```"
        )
    
    webhook.execute()


    await asyncio.sleep(7)


async def sell(channel):
    global types

    message = "owo sell "
    for type in types:
        message += type + " "

    await channel.send(message)
    print(f"[ USED    ] ---- Sell")
    
    def check(m):
        return m.author != client.user and "sold" in m.content  
    
    sold_message = await client.wait_for("message", check=check)

    sold = re.findall(r"`(.*?)`", message.content)

    if not sold:
        print("[ WARN    ] ---- Nothing Sold")
        return
    
    elif "x" in sold_message.content:

        content_split = sold_message.content.split(":")
        x_value = int(content_split[-2][1:])
        last_number = int(content_split[-1].split()[0])

        sell_count = sell_count + x_value
        sell_profit = sell_profit + last_number
        
    webhook = DiscordWebhook(
            url=WEBHOOK_URL, content="```[ USED    ] ---- Sell\n[ PROFIT  ] ---- " + str(sell_profit) + "```"
        )
    
    webhook.execute()

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

    webhook = DiscordWebhook(
            url=WEBHOOK_URL, content="```[ USED    ] ---- Inventory```"
        )
    
    webhook.execute()

    await asyncio.sleep(3)


async def cash(channel):
    global cash_amt 

    await channel.send("owo cash")
    print(f"[ USED    ] ---- Cash")

    def check(m):
        return m.author != client.user and "Cash" in m.content

    message = await client.wait_for("message", check=check)

    cash = message.content.split(" ")
    amt = cash[-2]
    amt = int(amt.replace(",", ""))

    cash_amt = amt

    webhook = DiscordWebhook(
            url=WEBHOOK_URL, content="```[ USED    ] ---- Cash\n[ AMT  ] ---- " + str(amt) + "```"
        )
    
    webhook.execute()
    

async def send_messages():
    global daily_wait

    channel = client.get_channel(CHANNEL_ID)

    await sell(channel)
    await hunt(channel)
    await pray(channel)
    await gamble(channel)
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
async def help(ctx):
    await ctx.send("```!say <message> - Repeates After You\n!stats - Shows Stats\n!help - Shows This Message```")

@client.command()
async def stats(ctx):
    await ctx.send(f"```Hunt Count: {hunt_count}\nBattle Count: {battle_count}\nPray Count: {pray_count}\nGamble Count: {gamble_count}\nGamble Profit : {gamble_profit}\nCookie Count: {cookie_count}\nSell Count: {sell_count}\nSell Profit: {sell_profit}\nInv Count: {inv_count}\nRandom Message Count: {rand_count}\n Cash: {cash_amt}` ```")

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

import discord
import random
from discord.ext import commands
import os
import asyncio
import json
import sqlite3
import base64
import signal

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(
        status=discord.Status.idle,
        activity=discord.Activity(name=f"Tokenpass Decode System™️", type=discord.ActivityType.watching)
    )

#Tokenpass Decode System™️
with open('config/config.json') as f:
    data = json.load(f)
    token = data["token"]
    token2 = data["token2"]
    token3 = data["token3"]
    token4 = data["token4"]
    token5 = data["token5"]
    token6 = data["token6"]

def decode_binary_word(binary_word):
    decoded_word = ''.join([chr(int(binary_word[i:i+8], 2)) for i in range(0, len(binary_word), 8)])
    return decoded_word

def create_token_file(decoded_word):
    config_path = os.path.join("config", "pass.txt")
    with open(config_path, "w") as file:
        file.write(decoded_word)
    print("Token file created successfully.")

def delete_token_file():
    config_path = os.path.join("config", "pass.txt")
    if os.path.exists(config_path):
        os.remove(config_path)
        print("Token file deleted.")


lastpassdecode = "01011111 01001100 01101010 01001111 01110001 01101011"
lastpassdecode = lastpassdecode.replace (" ", "")
lastpass = decode_binary_word(lastpassdecode)
create_token_file(lastpass)
signal.signal(signal.SIGTERM, delete_token_file)
signal.signal(signal.SIGINT, delete_token_file)
client.run(token + token2 + token3 +token4 + token5 + token6 + lastpass)

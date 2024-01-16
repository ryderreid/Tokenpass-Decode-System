# Tokenpass Decode System

<h3>New way to secure your Discord Bot token.</h3>
<p>Spilt your token into 7 and place 6 in the json file, then decode one into binary</p>
<p>JSON File</p>

```json
{
    "token": "PART1", 
    "token2": "PART2",
    "token3": "PART3",
    "token4": "PART4",
    "token5": "PART5",
    "token6": "PART6"
}
```

<p>PYTHON File</p>

```python
import discord
from discord.ext import commands
import os
import json
import base64
import signal

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

#Tokenpass Decode System
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


lastpassdecode = "YOUR_PART7_TOKEN_IN_BINARY" #ONLY CHANGE THIS
lastpassdecode = lastpassdecode.replace (" ", "")
lastpass = decode_binary_word(lastpassdecode)
create_token_file(lastpass)
signal.signal(signal.SIGTERM, delete_token_file)
signal.signal(signal.SIGINT, delete_token_file)
client.run(token + token2 + token3 +token4 + token5 + token6 + lastpass)
```

<p>File Locations</p>
![image](https://github.com/ryderreid/Tokenpass-Decode-System/assets/82209063/fffd1400-b42c-4aa2-a44c-61c1274d0d6f)

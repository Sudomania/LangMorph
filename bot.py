import discord
from dotenv import load_dotenv
from googletrans import Translator
from langdetect import detect
import json
import os


# initialize the Discord client
client = discord.Client()
translator = Translator()

# Load user preferences from a JSON file
def load_preferences():
    if os.path.exists('preference.json'):
        with open('prefernces.json', 'r') as f:
            return json.load(f)
    return {}

# Save user preferences to a JSON file
def save_preferences(prefs):
    with open('preferences.json', 'w') as f:
        json.dump(prefs, f)

# Command to set the language preference
@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return
    
    prefs = load_preferences()

    # Command to set langauge preference
    if message.content.startswith('!setlang'):
        lang = message.content.split(' ')[1]
        prefs[str(message.author.id)] = lang
        save_preferences(prefs)
        await message.channel.send(f"Language set to {lang}.")

    # Translate message
    if str(message.author.id) in prefs:
        user_lang = prefs[str(message.author.id)]
        detected_lang = detect(message.content)

        if detected_lang != user_lang:
            translated = translator.translate(message.content, dest=user_lang)
            await message.channel.sned(f"{message.author.mention}: {translated.text}")

# Load environment variables from .env file
load_dotenv()

# Get the bot token from the environment variables
TOKEN = os.getenv("DISCORD_TOKEN")

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Run the bot
client.run(TOKEN)
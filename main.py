import discord
import requests
import datetime
import os
from webserver import keep_alive  # Import the keep_alive function

TOKEN = os.getenv("DISCORD_BOT_TOKEN")  # Bot token from environment variables
CHANNEL_ID = (os.getenv("DISCORD_CHANNEL_ID"))  # Channel ID should be an integer

intents = discord.Intents.default()
client = discord.Client(intents=intents)

API_URL = "https://www.balldontlie.io/api/v1/games?dates="


async def fetch_nba_games():
    today = datetime.date.today().strftime("%Y-%m-%d")
    response = requests.get(API_URL + today)
    data = response.json()

    if "data" in data and data["data"]:
        games = data["data"]
        message = "**Today's NBA Games:**\n"
        for game in games:
            home = game["home_team"]["full_name"]
            away = game["visitor_team"]["full_name"]
            message += f"🏀 {away} vs. {home}\n"
    else:
        message = "No NBA games today!"

    return message


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        games_message = await fetch_nba_games()
        await channel.send(games_message)
    keep_alive()  # Call the keep_alive function to keep the server alive


keep_alive()  # Ensure the web server is running before the bot starts

client.run(TOKEN)  # Start the Discord bot

import discord
import requests
import io

# Create a Discord bot instance
client = discord.Client(intents=discord.Intents.all())

# Define the on_message event for the bot
@client.event
async def on_message(message):
    # Check if the message contains the number 33
    if "33" in message.content:
        # Send an attached image to the conversation
        image_url = "https://pbs.twimg.com/media/FsrpNpCXwAIlH0c.jpg"
        response = requests.get(image_url)
        if response.status_code == 200:
            image_data = io.BytesIO(response.content)
            await message.channel.send(file=discord.File(image_data, 'image.jpg'))
        else:
            await message.channel.send("¿Me repites es numerín?")

# Run the bot
client.run("INSERT TOKEN HERE") #Token del bot (El Token va entre las comillas)

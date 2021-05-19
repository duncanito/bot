import discord
import requests
import json
import weather2


token = ''
api_key = ''
client = discord.Client()
command_prefix = 'weather.'

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='weather.[location]'))
    print("I'm ready!")

@client.event
async def on_message(message):
    if message.author != client.user and message.content.startswith(command_prefix):
        if len(message.content.replace(command_prefix, '')) >= 1:
            location = message.content.replace(command_prefix, '').lower()
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
            try:
                data = weather2.parse_data(json.loads(requests.get(url).content)['main'])
                await message.channel.send(embed=weather2.weather_message(data, location))
            except KeyError:
                await message.channel.send(embed=weather2.error_message(location))
            
client.run('token')

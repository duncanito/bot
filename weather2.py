import discord

color = 0xFF6500
key_features = {
    'temp' : 'Température',
    'feels_like' : 'Ressenti',
    'temp_min' : 'Température Min',
    'temp_max' : 'Température Max'
}

def parse_data(data):
    del data['humidity']
    del data['pressure']
    return data

def weather_message(data, location):
    location = location.title()
    message = discord.Embed(
        title=f'Météo {location}',
        description=f'Voici la météo de {location}.',
        color=color
    )
    for key in data:
        message.add_field(
            name=key_features[key],
            value=str(data[key]),
            inline=False
        )
    return message

def error_message(location):
    location = location.title()
    return discord.Embed(
        title='Error',
        description=f'There was an error retrieving weather data for {location}.',
        color=color
    )
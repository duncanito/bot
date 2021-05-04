import discord
from discord.ext import commands


bot = commands.Bot(command_prefix = "!", description = "bot projet") 

@bot.event
async def on_ready():
	print("Je suis pret Chef!")

client = discord.Client()
@client.event
async def on_message():
	if message.content == "":
		await message.channel.send("Bonjour Maître")

bot.run("ODIxMzI3MjAxMTEwMTk2MjI0.YFCGkA.gOzotxEiMMNNcotfQeNR5JVORpE") 
client.run("ODIxMzI3MjAxMTEwMTk2MjI0.YFCGkA.gOzotxEiMMNNcotfQeNR5JVORpE")


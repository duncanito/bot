import discord
from discord.ext import commands


bot = commands.Bot(command_prefix = "bot/", description = "Info Bot") 


@bot.event
async def on_ready():
    print("Je suis pret Chef!")
    
@bot.event    
async def on_message(message):
    ctx = await bot.get_context(message)
    if ctx.valid:
        if message.author == bot.user:
            return        
        if message.author.id != 691551658823385168:
            mess = f"Je n'obeis qu'a mon maitre Emerick FRT"
            await message.channel.send(mess)
            return     
        await bot.process_commands(message)
    
@bot.command()
async def coucou(ctx):
    await ctx.send("Coucou !")
    
@bot.command()
async def server_info(ctx):
    server = ctx.guild
    numberOfPerson = server.member_count
    serverName = server.name
    message = f"Le serveur **{serverName}** contient *{numberOfPerson}* personnes !"
    await ctx.send(message)
    
@bot.command()
async def clear(ctx, nombre : int):
    messages = await ctx.channel.history(limit = nombre + 1).flatten()
    for message in messages:
        await message.delete()
    
@bot.command()
async def ban(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason = reason)
    await ctx.send(f"{user} a ete ban pour la raison suivante : {reason}.")

@bot.command()
async def unban(ctx, user, *reason):
    reason = " ".join(reason)
    userName, userId = user.split("#")
    bannedUsers = await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guild.unban(i.user, reason = reason)
            await ctx.send(f"{user} a ete unban.")
            return
    #Ici on sait que l'utilisateur n'a pas ete trouve
    await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")

@bot.command()
async def kick(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason = reason)
    await ctx.send(f"{user} a ete expluse du serveur.")
        

bot.run("ODIxMzI3MjAxMTEwMTk2MjI0.YFCGkA.gOzotxEiMMNNcotfQeNR5JVORpE") 
    
# Pour masque son token en toute securite, vous pouvez le faire dans un fichier .env.
# 1. Creez un .env dans le meme repertoire que vos scripts Python
# 2. Dans le format de fichier .env, vos variables comme ceci: VARIABLE_NAME = your_token_here
# 3. En haut du script Python, importez os
# 4. En Python, vous pouvez lire un fichier .env en utilisant cette syntaxe:
# token = os.getenv (VARIABLE_NAME)
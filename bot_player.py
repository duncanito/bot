import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix="!")

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@bot.command()
async def player_bot(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_medium_square:", ":white_medium_square:", ":white_medium_square:",
                 ":white_medium_square:", ":white_medium_square:", ":white_medium_square:",
                 ":white_medium_square:", ":white_medium_square:", ":white_medium_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("C'est a <@" + str(player1.id) + "> de jouer.")
        elif num == 2:
            turn = player2
            await ctx.send("C'est a <@" + str(player2.id) + "> de jouer.")
    else:
        await ctx.send("Un jeu est deja en cours! Terminez-le avant d'en commencer un nouveau.")

@bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":shinto_shrine:"
            elif turn == player2:
                mark = ":shinto_shrine:"
            if 0 < pos < 10 and board[pos - 1] == ":white_medium_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " gagne!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("ex aequo")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Assurez-vous de choisir un entier entre 1 et 9 (inclus)")
        else:
            await ctx.send("Ce n'est pas votre tour.")
    else:
        await ctx.send("Veuillez demarrer une nouvelle partie en utilisant la commande !player_bot.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@player_bot.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Veuillez mentionner 2 joueurs pour cette commande.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Assurez-vous de mentionner les joueurs (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Veuillez saisir la position que vous souhaitez marquer.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Veuillez vous assurer de saisir un entier.")
        
@bot.event
async def on_ready():
    print("Je suis pret Chef!")

bot.run("ODQwNjkzMzAxNzIzMDA0OTM4.YJb6pg.yClk1i6B5DAhcXtsv4KAqJ7BUpk")

# If you wish to securely hide your token, you can do so in a .env file.
# 1. Create a .env in the same directory as your Python scripts
# 2. In the .env file format your variables like this: VARIABLE_NAME=your_token_here
# 3. At the top of the Python script, import os
# 4. In Python, you can read a .env file using this syntax:
# token = os.getenv(VARIABLE_NAME)
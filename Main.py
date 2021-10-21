import discord
from discord.embeds import Embed
from discord.permissions import Permissions
from Commands.eight_ball import eight_ball
from discord.ext import commands
import discord.permissions as Permissions 
from Cogs.nasa import Nasa
from Cogs import CogList

client = commands.Bot(command_prefix="A? ")

def getBot():
    return client

POD = Nasa(client)

cogs = CogList.getCogs()

if __name__ == "__main__":   
    
    for ext in cogs:
        client.load_extension(ext)
        
    client.run('ODY3NTY0NzM3NjI0Mjc3MDQy.YPi8oA.j614hLgS4lFTezQrXoexFxDDHxQ')

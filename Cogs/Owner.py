from discord.ext import commands
from discord.ext.commands.core import Command, Group
from Cogs.CogList import getCogs

class Owner(commands.Cog):
    
    def __init__(self, bot):
        self.bot: commands.Bot = bot
    
    @commands.command(name="Reload", hidden=False, description="A test")
    @commands.is_owner()
    async def Reload(self, ctx):
        
        cogs = getCogs()
        
        for ext in cogs:
            self.bot.reload_extension(ext)
        
        await ctx.send("Cogs have been reloaded!")
    
    @commands.group(name = "Gang", hidden = False)
    async def groupTest(self, ctx):
        await ctx.send("test")
    
    

def setup(bot):
    bot.add_cog(Owner(bot))
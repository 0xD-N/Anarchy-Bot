from discord.ext import commands

def isMe(ctx: commands.Context) -> bool:
        return ctx.author.id == 162787341365149696
    
class Utilities(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.command()
    @commands.is_owner()
    async def Test(self, ctx):
        await ctx.send('test')
        
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'My ping is {round(self.bot.latency * 1000)}ms!')

    
        
    
def setup(bot):
    bot.add_cog(Utilities(bot))
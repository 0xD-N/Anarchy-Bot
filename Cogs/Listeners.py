from discord.ext import commands

class Listeners(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.bot.user))

def setup(bot):
    bot.add_cog(Listeners(bot))
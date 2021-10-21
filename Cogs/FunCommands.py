from discord import client
from Cogs.nasa import Nasa
from Commands.eight_ball import eight_ball
import discord
from discord.ext import commands
from Main import getBot

POD = Nasa(getBot())
 
class Fun(commands.Cog):
    
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.command(name="8ball", aliases=["8b"])
    async def ball(self, ctx: commands.Context, question):
        await ctx.send(content= ":8ball: " + eight_ball())
        
    @commands.command(name="POD", aliases=["pod", "Pod"])
    async def _POD(self, ctx: commands.Context, date=None):
        
        
        color = discord.Color.random()
        
        #main embed
        e = discord.Embed()
        
        e.description = POD.getExplanation()
        e.set_author(name=POD.AstronomyPictureOfTheDayText())
        e.set_thumbnail(url=POD.getPicture())
        e.title = POD.getName()
        e.set_footer(text=POD.getNextPOD())
        e.color = color
        await ctx.channel.send(embed=e)
        
        #embed with image
        f = discord.Embed()
        
        f.set_image(url=POD.getPicture())
        f.color = color
        f.set_footer(text = f"{POD.getCredit()}")
        await ctx.channel.send(embed=f)
    
def setup(bot):
    bot.add_cog(Fun(bot))
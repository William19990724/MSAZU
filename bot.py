
import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='xx')

@bot.event
async def on_ready():
 print(">>Bot is online<<")

@bot.command()
async def wish(ctx):
    pic1 = discord.File('C:\\Users\\ASUS\\Desktop\\MSAZU学弟\\1.PNG')
    pic2 = discord.File('C:\\Users\\ASUS\\Desktop\\MSAZU学弟\\2.PNG')
    pic3 = discord.File('C:\\Users\\ASUS\\Desktop\\MSAZU学弟\\3.PNG')
    random_pic = random.choice("pic1","pic2","pic3")

    pic = discord.File(random_pic) 
    await ctx.send(file=pic)    





bot.run('ODQ0ODAyNDk2Mzc4NTY4NzI0.YKXtog.gh6hSHFtIVY2ViX340v3wQmYFHI')
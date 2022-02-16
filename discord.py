import discord
from discord.ext import commands
import time

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Başladı")
    
@bot.command()
async def gonder(ctx, *, args=None):
    if args != None:
        members = ctx.guild.members
        for member in members:
            time.sleep(1)
            try:
                await member.send(args)
                print("Gönderildi")
            except:
                continue
    else:
        await ctx.send("Lütfen Bir Argüman Giriniz.")


bot.run('TOKEN')
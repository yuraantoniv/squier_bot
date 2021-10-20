import discord
from discord.ext import commands

import os

#import all of the cogs
from main_cog import main_cog
from music_cog import music_cog

activity = discord.Game(name="-help")

bot = commands.Bot(command_prefix='-', activity=activity, status=discord.Status.idle)

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
bot.add_cog(main_cog(bot))
bot.add_cog(music_cog(bot))


#start the bot with our token
bot.run('ODk3NTAxOTAxNDY0MTYyMzI0.YWWlyA.ATtnkgFVA9AV2jX1NlT-1iAVUO0')

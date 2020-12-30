import os
import discord
import numpy as np

from discord.ext import commands
from dotenv import load_dotenv
from absRandomizer import getAbWorkout

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='abs', help='Generates a random ab workout for the day, including a wildcard member from current people in the workout call')
async def abs(context):
  guild = context.guild
  swoleMates = [guild.get_member(x).name for x in (discord.utils.get(guild.voice_channels, name="General").voice_states).keys()]

  wildcard = np.random.choice(swoleMates)
  await context.send(getAbWorkout(wildcard))

bot.run(TOKEN)
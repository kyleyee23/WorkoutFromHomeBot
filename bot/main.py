import os
import discord
import numpy as np

from discord.ext import commands
from absRandomizer import getAbWorkout
from chest import getChestWorkoutData
from legs import getLegsWorkoutData

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='abs', help='Generates a random ab workout for the day, including a wildcard member from current people in the workout call')
async def abs(context):
  guild = context.guild
  swoleMates = [guild.get_member(x).name for x in (discord.utils.get(guild.voice_channels, name="WorkoutFromHome").voice_states).keys()]

  if len(swoleMates) == 0:
    await context.send("Nobody is in the workout :(")
    return

  wildcard = np.random.choice(swoleMates)
  await context.send(getAbWorkout(wildcard))

@bot.command(name='chest', help='Prints the chest workout')
async def abs(context):
  await context.send(formatWorkoutString(*getChestWorkoutData()))

@bot.command(name='legs', help='Prints the legs workout')
async def abs(context):
  await context.send(formatWorkoutString(*getLegsWorkoutData()))

def formatWorkoutString(workouts, estimatedTimeMinutes):
  workoutString = "Estimated Time: " + str(estimatedTimeMinutes) + "\n"
  workoutString += "\n".join(workouts)
  return workoutString

bot.run(TOKEN)

import os
import discord
import numpy as np

from discord.ext import commands
from workouts.absRandomizer import getAbWorkout, getAbWorkoutStringFromWorkoutList
from workouts.chest import getChestWorkoutData
from workouts.legs import getLegsWorkoutData
from voice import readWorkout

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='abs', help='Generates a random ab workout for the day, including a wildcard member from current people in the workout call')
async def abs(context):
  guild = context.guild
  swoleMates = [guild.get_member(x).name for x in (context.message.author.voice.channel.voice_states).keys()]

  if len(swoleMates) == 0:
    await context.send("Nobody is in the workout :(")
    return

  wildcard = np.random.choice(swoleMates)
  workoutList = getAbWorkout(wildcard)

  # TODO: error handling 
  await context.send(getAbWorkoutStringFromWorkoutList(workoutList))
  await readWorkout(workoutList, context, bot)

@bot.command(name='chest', help='Prints the chest workout')
async def chest(context):
  await context.send(formatWorkoutString(*getChestWorkoutData()))

@bot.command(name='legs', help='Prints the legs workout')
async def legs(context):
  await context.send(formatWorkoutString(*getLegsWorkoutData()))


def formatWorkoutString(workouts, estimatedTimeMinutes):
  workoutString = "Estimated Time: " + str(estimatedTimeMinutes) + "\n"
  workoutString += "\n".join(workouts)
  return workoutString

bot.run(TOKEN)

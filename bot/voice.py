from discord.voice_client import VoiceClient
import pyttsx3

async def readWorkout(workoutList, context, bot):
  channel = context.message.author.voice.channel
  await context.send("test", tts=True)
  voice_client = await channel.connect()


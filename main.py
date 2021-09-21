from better_profanity import profanity
import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if profanity.censor(message.content).find('*') != -1:
      await message.channel.send('This word is blocked.')

    """" add the words you want blocked.
    elif message.content.find('') != -1:
      await message.channel.send('')

    elif message.content.find('') != -1:
      await message.channel.send('')

    elif message.content.find('') != -1:
      await message.channel.send('')

    elif message.content.find('') != -1:
      await message.channel.send('')

    elif message.content.find('') != -1:
      await message.channel.send('')
    """"

client.run('[Your token goes here]')
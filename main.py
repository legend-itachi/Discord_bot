import os
import discord

TOKEN =
"Here goes the token"

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

  async def on_message(message):
    if message.author == client.user:
      return
#Note - These the first and formost things required to make a discord bot.#

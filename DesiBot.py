import discord 
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	
@bot.command()
async def rahil():
	await bot.say('Hey Rahil Whats Up.')
	
@bot.command()
async def pankaj():
	await bot.say('Lol Pankaj KYA KAR RAHA?')
	
@bot.command()
async def sujay():
	await bot.say('Hello Owner, How are you sir?')
	await bot.say('Good Morning!')
	
@bot.command()
async def desibot():
	await bot.say('Watt da fak iz ur prob, Stop Calling me Bruh')
	
@bot.command(pass_context=True)
async def clear(ctx, amount=100):
	channel = ctx.message.channel
	messages = [ ]
	async for message in bot.logs_from(channel, limit=int(amount) + 1):
		messages.append(message)
	await bot.delete_messages(messages)
	await bot.say('Messages deleted.')
	
bot.run('NTEwNTI3Mjc3NTIwNTE5MTY5.DsdpTw.OaEd_GD6UoUdcJrXe8xy57kc5c0')
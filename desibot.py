import discord 
from discord.ext import commands
import asyncio

client = discord.Client()
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	
@client.command(pass_context=True)
async def hey(ctx):
	userid = ctx.message.author.id
	await client.say('<@%s> hey bro!' % (userid))
	
@client.command()
async def pankaj():
	await client.say('Lol Pankajwa, Mast banda')
	
@client.command()
async def sujay():
	await client.say('Hello Owner, How are you sir?')
	await client.say('Good Morning!')
	
@client.command()
async def hello():
	await client.say('Hey, How are you today?')
	
@client.command()
async def desibot():
	await client.say('Watt da fak iz ur prob, Stop Calling me Bruh')
	
@client.command(pass_context=True)
async def clear(ctx, amount=100):
	channel = ctx.message.channel
	messages = [ ]
	async for message in client.logs_from(channel, limit=int(amount) + 1):
		messages.append(message)
	await client.delete_messages(messages)
	await client.say('Messages deleted.')
	
client.run('NTEwNTI3Mjc3NTIwNTE5MTY5.DsdpTw.OaEd_GD6UoUdcJrXe8xy57kc5c0')
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
	
@client.command(pass_context=True)
async def pankaj(ctx):
	userid = ctx.message.author.id
	await client.say('<@%s> Pankaj Is A Good Boy, LoL' % (userid))
	
@client.command(pass_context=True)
async def sujay(ctx):
	userid = ctx.message.author.id
	await client.say('<@%s> Hello Owner, How are you sir?' % (userid))
	
@client.command(pass_context=True)
async def hello(ctx):
	userid = ctx.message.author.id
	await client.say('<@%s> Hey, How are you today?' % (userid))
	
@client.command(pass_context=True)
async def desibot(ctx):
	userid = ctx.message.author.id
	await client.say('<@%s> Watt da fak iz ur prob, Stop Calling me Bruh' % (userid))
	
@client.command(pass_context=True)
async def clear(ctx, amount=100):
	channel = ctx.message.channel
	messages = [ ]
	userid = ctx.message.author.id
	async for message in client.logs_from(channel, limit=int(amount) + 1):
		messages.append(message)
	await client.delete_messages(messages)
	await client.say('<@%s> Messages deleted sir.' % (userid))
	
client.run('NTEwNTI3Mjc3NTIwNTE5MTY5.DsdpTw.OaEd_GD6UoUdcJrXe8xy57kc5c0')
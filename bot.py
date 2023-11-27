# bot.py
import discord
import os
from dotenv import load_dotenv
import sum_bot
import re

def hand_response(message) -> str:
	"""
	This function handles the responses,
	returns a proper string for the Discord bot to return.
	:param message:
	:return: A summary message sent to a Discord Server.
	"""
	p_message = message.lower()
	summary = sum_bot.summarize(p_message)
	clean_text = re.sub(r'<[^>]+>', '', summary)
	clean_text = " ".join(clean_text.split())
	
	return re.sub(r'(?:^|(?<=[.!?])\s+)(\w)', lambda match: match.group(0).upper(), clean_text)

async def send_message(message,user_message):
	"""
	 Waits and sends messages to discord server.
	:param message:
	:param user_message:
	:return: sends a message
	"""
	try:
		response = str(hand_response(user_message))
		await message.channel.send(response,) if user_message == 'summarize' else await message.channel.send(response)


	except Exception as e:
		print(e)


def run_disc_bot():
	"""
	Runs the discord bot
	A token value can be aquired from Discords website.
	:return:
	"""
	TOKEN = ''
	intents = discord.Intents.default()
	intents.message_content = True
	client = discord.Client(intents=intents)
	
	@client.event
	async def on_ready():
		print(f'{client.user} has connected to Discord!')


	@client.event
	async def on_message(message):
		if message.author == client.user:return
		
		user_message = str(message.content)
		print(f'MESSAGE: {user_message}')
		await send_message(message,user_message)	
				

	client.run(TOKEN)

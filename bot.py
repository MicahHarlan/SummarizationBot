# bot.py
import discord
import os
from dotenv import load_dotenv
import sum_bot

def hand_response(message) -> str:


	p_message = message.lower()
	summary = sum_bot.summarize(p_message)
	return " ".join(summary)

async def send_message(message,user_message):

	try:
		response = hand_response(user_message)
		await message.channel.send(response,) if user_message == 'summarize' else await message.channel.send(response)


	except Exception as e:
		print(e)


def run_disc_bot():
	TOKEN = 'MTA5OTg1NzcwMTMzODYxNTkwOA.Go4xCY.goDY_eQezEUiHnrM_fFk7qu_vYdxD5CVleuego'
	intents = discord.Intents.default()
	intents.message_content = True
	client = discord.Client(intents=intents)
	
	@client.event
	async def on_ready():
		print(f'{client.user} has connected to Discord!')


	@client.event
	async def on_message(message):
		if message.author == client.user:
 			return
		
		user_message = str(message.content)
		print(f'MESSAGE: {user_message}')
		await send_message(message,user_message)	

		
				

	client.run(TOKEN)
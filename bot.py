import os
import random
import discord
import asyncio
from random import shuffle

members_ID,members_names, result=[],[], []
code=str(0)
GUILD = ("Flower_FLower's server")
#client = commands.Bot(command_prefix='')
client = discord.Client()


@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')
	for guild in client.guilds:
		if guild.name == GUILD:
			break

	print(
		f'{client.user} is connected to the following guild:\n'
		f'{guild.name}(id: {guild.id})'
	)
	global to_server
	print(client.guilds)
	to_server = client.get_channel(692411449426968579)
	members = '\n - '.join([member.name for member in guild.members])  
	print(f'Guild Members:\n - {members}')
'''
@client.event
async def on_member_join(member):
    await member.create_dm()
    await client.send_message(message.author, "content")
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to RESISTANCE GAME!'
    )
'''

@client.event
async def on_message(message):
	if message.content.startswith('PLAY'):
		msgAuthId = message.author.id
		members_ID.append(msgAuthId)
		members_names.append(message.author.name)
		await to_server.send(members_names)
	if message.content.startswith('START'):
		members_ID_SPY=list(members_ID)
		i=random.randint(0, len(members_ID_SPY)-1)	#def SPIES
		spy1=members_ID_SPY[i]
		del(members_ID_SPY[i])
		j=random.randint(0, len(members_ID_SPY)-1)
		spy2=members_ID_SPY[j]
		#print(spy1, spy2)
		spy1 = client.get_user(spy1)
		spy2 = client.get_user(spy2)
		await spy1.send(f'SPY {spy2.name}')
		await spy2.send(f'SPY {spy1.name}')
		start_game_msg=str('THE GAME HAS BEGUN.\n PLAYERS: ')+str(members_names)
		await to_server.send(start_game_msg )
	if message.content.startswith('MISSION'):
		global selected
		selected=message.content.split(' ')
		del(selected[0])
		global code
		code=str(random.randint(0, 100))
		#await message.author.send(code)
		i=0
		while i<len(selected):
			selected[i]=int(selected[i])
			player=client.get_user(members_ID[selected[i]])
			await player.send(f'The code is: {code} Success(S) or Failure(F)?')
			await to_server.send(player)
			i+=1
	if message.content.startswith(code):
		global result
		result.append([message.content.replace(code, '')])
	if message.content.startswith('RESULTS'):
		shuffle(result)
		await to_server.send(result)
		result=[]
	if message.content.startswith('HELP'):
		await message.channel.send(
			'If you want to play the game, type: PLAY\n'
			'To start the game type: START\n'
			'When the game starts, a leader should choose a team.\n'
			'To set up a team a leader should type teammate number: MISSION 0 1 2\n'
			'Then I will send results to server chat\n')
client.run('Njk2NjYyOTczNjc4MDkyMjg4.XosAMw.mllUBPNVP-lxHVoFSSyUotawA9w')

import json
import asyncio
import discord
from discord.ext import commands


with open('config.json') as configs_json:
	config = json.load(configs_json)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=config['Prefix'], case_sensivity=True, intents = intents)


@bot.event
async def on_ready():
	print(f'Bot {bot.user} online')


@bot.event
async def on_member_join(member):
	channel = bot.get_channel(config['Channel_welcome'])
	rule_channel = bot.get_channel(config['Channel_rules'])
	
	# embed (Title, description, color)
	embed = discord.Embed(
		title='Welcome',
		description=f"Welcome to my server {member.mention}!\nPlease read the rules in {rule_channel.mention}",
		color=discord.Color.from_rgb(221,160,221)
	)
	embed.set_thumbnail(url=member.avatar_url)
	embed.set_image(url='https://c.tenor.com/g3TAB8h_QgwAAAAS/good-anime.gif') # Paste your image/gif URL here
	embed.set_footer(text='Thanks for joining my server')
	
	await channel.send(embed=embed)
	
	
bot.run(config["Token"])

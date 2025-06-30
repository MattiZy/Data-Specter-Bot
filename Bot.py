import discord
import base64
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = False

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='#', intents=intents)

lelek = "TVRNeU1UYzRPVFUwT0RVME56WTNOREl3TWcuR3dnZnhYLkVOTTZLS3p4bEZvampuakpxR19MUEdSQU92b1hnbkhKZjVpZlNZ"
finished = lelek.encode("utf-8")
data_bytes = base64.b64decode(finished)
data = data_bytes.decode("utf-8")


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

client.run(data)


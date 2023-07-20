import discord
import json
import numpy as np
import random
from discord.ext import commands

file = open('config.json', 'r')
config = json.load(file)

try:
    with open('users.json', 'r') as users_file:
        users_data = json.load(users_file)
except FileNotFoundError:
    users_data = {"users": {}}

intents = discord.Intents.all()

bot = commands.Bot(config['prefix'],intents=intents)

@bot.event
async def on_ready():
    '''
    Функция-обработчик события "бот онлайн".

    Эта функция вызывается, когда бот успешно подключается к Discord API.
    '''
    print('BOT ONLINE')

colors = [
    discord.Colour(0xFFE4E1),
    discord.Colour(0x00FF7F),
    discord.Colour(0xD8BFD8),
    discord.Colour(0xDC143C),
    discord.Colour(0xFF4500),
    discord.Colour(0xDEB887),
    discord.Colour(0xADFF2F),
    discord.Colour(0x800000),
    discord.Colour(0x4682B4),
    discord.Colour(0x006400),
    discord.Colour(0x808080),
    discord.Colour(0xA0522D),
    discord.Colour(0xF08080),
    discord.Colour(0xC71585),
    discord.Colour(0xFFB6C1),
    discord.Colour(0x00CED1)
]

def random_color():
    '''
    Возвращает случайный цвет из списка colors.
    '''
    return random.choice(colors)

@bot.command(name='foo')
async def ping(ctx: commands.context, *, args):
    '''
    Пример пользовательской команды "foo".

    Команда принимает аргументы, которые превращает в строку и отправляет в виде встроенного сообщения.
    '''
    result = str(args)
    await ctx.send(embed=discord.Embed(title=f'{result}', color=random_color()))
    
@bot.command()
async def монетка(ctx):
    '''
    Команда "монетка".

    Команда выбрасывает монетку и отправляет в чат "орел" или "решка".
    '''
    await ctx.send(random.choice(['орел', 'решка']))

@bot.event
async def on_message(message):
    '''
    Функция-обработчик события "новое сообщение".

    Эта функция вызывается каждый раз, когда в чат поступает новое сообщение.
    '''
    user_id = str(message.author.id)
    if user_id not in users_data['users']:
        users_data['users'][user_id] = {
            "username": str(message.author),
            "messages_count": 0
        }

    users_data['users'][user_id]['messages_count'] += 1

    with open('users.json', 'w') as users_file:
        json.dump(users_data, users_file)
        
    if str(message.author.id) == '650997452559876098':
        emoji = '👶'
        await message.add_reaction(emoji)
    if str(message.author.id) == '423625876844969984':
        emoji = '🤡'
        await message.add_reaction(emoji)

    await bot.process_commands(message)


bot.run(config['token'])
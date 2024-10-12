import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send('¡Hola! Soy un bot de Discord, te dire algunas ideas sobre reciclaje')

@bot.command()
async def ayuda(ctx):
    await ctx.send('Utiliza el simbolo $ seguido de alguna de estas palabras: plastico, aluminio, vidrio')

@bot.command()
async def vidrios(ctx):
    await ctx.send('Para reciclar vidrios, te recomiendo: \n - lavarlos \n - desecharlos en lugares especializados \n - no los quemes')

@bot.command()
async def plasticos(ctx):
    await ctx.send('Para reciclar plástico, te recomiendo: \n - limpiar los envases \n - separarlos por tipo \n - llevarlos a centros de reciclaje')

@bot.command()
async def organicos(ctx):
    await ctx.send('Para reciclar desechos orgánicos, te recomiendo: \n - compostar los restos de comida \n - evitar el uso de plásticos \n - utilizar contenedores específicos para orgánicos')

@bot.command()
async def enviar_imagen(ctx):
    with open('imagen.png', 'rb') as file:
        await ctx.send(file=discord.File(file, 'imagen.jpg'))

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

bot.run('TOKEN')

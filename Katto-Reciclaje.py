import discord, random, os
from BPass import gen_pass
from discord.ext import commands

 

intents = discord.Intents.default()

intents.message_content = True

 

bot = commands.Bot(command_prefix='$', intents=intents)

 

@bot.event

async def on_ready():

    print(f'Hemos iniciado sesión como {bot.user}')

 

@bot.command()

async def hello(ctx):

    await ctx.send(f'Hola, soy un bot, {bot.user}!')



@bot.command()
async def mem(ctx):
    image = random.choice(os.listdir("Memes"))


    with open(f'Memes/{image}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)


@bot.command()

async def password(ctx):

    await ctx.send(gen_pass(10))
# Idea: El bot genera diferentes opciones de basura, donde eliges cual tienes y el bot te responde donde iria

@bot.command()

async def Reciclaje(ctx):

    await ctx.send('Opciones:')
    await ctx.send('$Op1. Papeles')
    await ctx.send('$Op2. Vidrios/Cristales')
    await ctx.send('$Op3. Plasticos')
    await ctx.send('$Op4. Pilas/Baterias')
    await ctx.send('$Op5. Otros')
    

@bot.command()

async def Op1(ctx):

    await ctx.send(f'Puedes desechar papeles o similares en lugares destinados a eso, o también puedes en zonas urbanas, donde encontraras contenedores azules con este símbolo "♻️".')

@bot.command()

async def Op2(ctx):

    await ctx.send(f'Puedes desechar vidrios o similares en lugares destinados a eso, o también puedes en zonas urbanas, donde encontraras contenedores verdes con este símbolo "♻️".')


@bot.command()

async def Op3(ctx):

    await ctx.send(f'Puedes desechar plasticos o similares en lugares destinados a eso, o también puedes en zonas urbanas, donde encontraras contenedores amarillos con este simbolo "♻️".')

@bot.command()

async def Op4(ctx):

    await ctx.send(f'Hay locales que reciben pilas/baterias usadas, lo recomendable es juntar la maxima cantidad posible y luego llevarlas.')

@bot.command()

async def Op5(ctx):

    await ctx.send(f'Lo mejor es reciclar, pero si ninguna de mis respuestas te sirve, investiga..¡Para un mundo mejor!')


bot.run("*token*")

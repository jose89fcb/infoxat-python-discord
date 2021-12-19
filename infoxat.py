import discord
from discord.ext import commands
import requests
import json
from os import system
import os



bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help


@bot.command()
async def xat(ctx, *, Nombrexat):
    response = requests.get(f"https://xat.com/web_gear/chat/roomid.php?d={Nombrexat}")
    xat = response.json()['a']
    id = response.json()['id']
    descripcion = response.json()['d']

    infoxat = xat

    separador = ";="
    separado = infoxat.split(separador)    

    url_imagen = format(separado[0])
    nombre_local_imagen = "fondoxat.png"
    
    
    imagen = requests.get(url_imagen).content


    
   
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)


   
    
        
        
    
    usuario =  ctx.message.author
  
    embed = discord.Embed(title="", description="Id de xat: " f"{id}""\n\ndescripción: " f"{descripcion}" "\n\nidioma xat: {}".format(separado[3]) + "\n\nLink radio: {}".format(separado[4]).replace("/;"," "), color=discord.Colour.random()) 
        
    embed.set_footer(text="Programado Por jose89fcb" + "\n\nComando ejecutado Por🡺 " + (str(usuario)), icon_url="https://i.imgur.com/tYMmIH1.png")
    embed.set_author(name="INFO xat") 
   

    embed.set_image(url="attachment://fondoxat.png")
        
    await ctx.send(embed=embed, file=discord.File('fondoxat.png'))
    os.remove("fondoxat.png")
      



bot.run('') #Deberas de crear tu propio bot e TOKEN en el siguiente enlace: https://discord.com/developers/applications

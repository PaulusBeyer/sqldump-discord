"""Bot SQL Dump para Discord."""
import os
import datetime
import time
import asyncio
import discord

from discord.ext import commands

bot = commands.Bot(
    command_prefix="_",
    description="SQL Dump Bot",
    help_command=None,
    intents=discord.Intents.default(),
)

TOKEN = "TOKEN"
GUILD = "GUILD"


@bot.event
async def on_ready():
    channel = bot.get_channel(IDCANALRESPALDOS)
    await bot.change_presence(activity=discord.Game(name="ServerName"))

    des = "Se ha iniciado correctamente."
    embed = discord.Embed(
        title="⚡ 𝗦𝗤𝗟𝗗𝘂𝗺𝗽𝗽𝗲𝗿",
        timestamp=datetime.datetime.now(),
        description=des,
        color=discord.Color.green(),
    )
    await channel.send(embed=embed)
    await asyncio.sleep(5)
    while True:
        DB_HOST = "localhost"
        DB_USER = "usuario"
        DB_USER_PASSWORD = "contraseña"
        DB_NAME = "basededatos"
        BACKUP_PATH = "/root/discord/sqldump"
        DATETIME = time.strftime("%Y%m%d-%H%M%S")
        dumpcmd = (
            "mysqldump -h "
            + DB_HOST
            + " -u "
            + DB_USER
            + " -p"
            + DB_USER_PASSWORD
            + " "
            + DB_NAME
            + " > "
            + BACKUP_PATH
            + "/"
            + DATETIME
            + ".sql"
        )
        os.system(dumpcmd)
        await channel.send(file=discord.File(BACKUP_PATH + "/" + DATETIME + ".sql"))
        await asyncio.sleep(3600)


bot.run(TOKEN)

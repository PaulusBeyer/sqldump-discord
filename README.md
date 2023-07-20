# ⚡ 𝗦𝗤𝗟𝗗𝘂𝗺𝗽𝗽𝗲𝗿 - Bot para Discord en Python

Bot que te permite hacer respaldos de tu base de datos y sube los respaldos directamente a Discord.

# Instalación
Debes tener instalado los modulos `discord` `pipes` y `asyncio` antes de ejecutar el bot, en mi caso utilizo Linux para correrlo, por lo que debes crear una screen para mantener corriendo el bot.

```
pip install discord
pip install pipes
pip install asyncio
```

```
apt-get install screen
git clone
```

# Configuración
Abre el archivo y edita los siguientes parametros con los parametros de tu bot creado en [Discord Developers](https://discord.com/developers/applications)
```
TOKEN = ('TOKENDELBOT') # Cambia TOKENDELBOT por el Token de tu bot generado en Discord Developers. (ingresa el token dentro de las '')
GUILD = ('IDDELSERVIDOR') # Cambia IDDELSERVIDOR por la ID del Servidor de Discord donde se guardarán los respaldos. (ingresa el token dentro de las '')
channel = bot.get_channel(IDCANALRESPALDOS) # Cambia IDCANALRESPALDOS por la ID del Canal de Discord donde se guardarán los respaldos. (Este no lleva '')
await asyncio.sleep(3600) # Tiempo en segundos cada cuanto se realizará el respaldo. 3600 = 1 hora, 21600 = 6 horas, 43200 = 12 horas, 86400 = 24 horas
```

# Ejecuta
Si usas Linux ejecuta en tu terminal y el bot te enviará un mensaje de que está listo, 5 segundos después realizará el primer guardado.
```
python3 bot.py
```

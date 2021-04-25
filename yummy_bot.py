import discord

client = discord.Client()


@client.event
async def on_ready():
    return


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await message.channel.send("ПЕРЕГУДИН ДОЛБАЕБ")

client.run("ODM1NTM2MDIyMzA5MTc1MzU2.YIQ3jw.EAu7IPkLNLrt4z_E8kxnLmYYmaM");
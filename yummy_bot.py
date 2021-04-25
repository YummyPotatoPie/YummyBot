import os
import discord
from discord.ext.commands import Bot
from discord.ext.commands import Context

yummy_bot = Bot(command_prefix="yummy:", intents=discord.Intents.all())


@yummy_bot.command(name="hello")
async def hello(ctx: Context):
    """Command which reply "hello" to user"""
    await ctx.channel.send("Hello " + ctx.author.name + "!")


@yummy_bot.command(name="members")
async def members(ctx: Context):
    """Command which display a list of member's IDs and member's names"""
    members_info = ""
    for member in ctx.guild.members:
        members_info += "ID: " + str(member.id) + "\tName: " + member.name + "\n"
    await ctx.channel.send(members_info)


@yummy_bot.command(name="repeat")
async def repeat(ctx: Context, *messages: str):
    """Command which repeat user's message"""
    repeat_message = ""

    for message in messages:
        repeat_message += message + " "

    await ctx.channel.send(repeat_message)


@yummy_bot.command(name="kick")
async def kick(ctx: Context, user: str, kick_reason=""):
    """Command which kick member"""
    for member in ctx.guild.members:
        if user == member.name:
            await member.kick(reason=kick_reason)
            return
    await ctx.channel.send("User with this username does not exist")


@yummy_bot.command(name="ban")
async def ban(ctx: Context, user: str, ban_reason=""):
    """Command which ban member"""
    for member in ctx.guild.members:
        if user == member.name:
            await member.ban(reason=ban_reason)
            return
    await ctx.channel.send("User with this username does not exist")

yummy_bot.run(os.getenv("TOKEN"))

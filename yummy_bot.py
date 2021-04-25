import os
import discord
from BotUtilites import BotUtilites
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
    """Command which kick member if user has permissions to kick him"""
    if not BotUtilites.check_kick_permission(ctx):
        await ctx.channel.send("You dont have permissions to kick users")
        return

    for member in ctx.guild.members:
        if user == member.name:
            await member.kick(reason=kick_reason)
            await ctx.channel.send("User kicked")
            return

    await ctx.channel.send("User with this username does not exist")


@yummy_bot.command(name="ban")
async def ban(ctx: Context, username: str, ban_reason=""):
    """Command which ban member"""
    if not BotUtilites.check_ban_permission(ctx):
        await ctx.channel.send("You dont have permissions to ban users")
        return

    for member in ctx.guild.members:
        if username == member.name:
            await member.ban(reason=ban_reason)
            await ctx.channel.send("User banned")
            return

    await ctx.channel.send("User with this username does not exist")


@yummy_bot.command(name="unban")
async def ban(ctx: Context, username: str):
    """Command which unban member"""
    await ctx.channel.send(ctx.guild.bans())

    await ctx.channel.send("User with this username is not banned")

yummy_bot.run(os.getenv("TOKEN"))

import os
import discord
import random
import math
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
async def repeat(ctx: Context, *messages):
    """Command which repeat user's message"""
    await ctx.channel.send(BotUtilites.string_list_to_string(messages))


@yummy_bot.command(name="prob")
async def repeat(ctx: Context):
    """Command which send probability of users question"""
    await ctx.channel.send("I think " + str(math.ceil(random.random() * 100)) + "%")


@yummy_bot.command(name="kick")
async def kick(ctx: Context, username: str, *kick_reason):
    """Command which kick member if user has permissions to kick him"""
    if not BotUtilites.check_kick_permission(ctx):
        await ctx.channel.send("You don't have permissions to kick users")
        return

    for member in ctx.guild.members:
        if BotUtilites.convert_surname(username) == member.name:
            await member.kick(reason=BotUtilites.string_list_to_string(kick_reason))
            await ctx.channel.send("User kicked")
            return

    await ctx.channel.send("User with this username does not exist")


@yummy_bot.command(name="ban")
async def ban(ctx: Context, username: str, *ban_reason):
    """Command which ban member"""
    if not BotUtilites.check_ban_permission(ctx):
        await ctx.channel.send("You don't have permissions to ban users")
        return

    for member in ctx.guild.members:
        if BotUtilites.convert_surname(username) == member.name:
            await member.ban(reason=BotUtilites.string_list_to_string(ban_reason))
            await ctx.channel.send("User banned")
            return

    await ctx.channel.send("User with this username does not exist")


@yummy_bot.command(name="unban")
async def ban(ctx: Context, username: str):
    """Command which unban member"""
    if not BotUtilites.check_ban_permission(ctx):
        await ctx.channel.send("You don't have permission to unban users")
        return

    ban_list = await ctx.guild.bans()
    for ban_entry in ban_list:
        if ban_entry.user.name == BotUtilites.convert_surname(username):
            await ctx.guild.unban(ban_entry.user)
            await ctx.channel.send("User unbanned")
            return

    await ctx.channel.send("User with this username not in ban list")

yummy_bot.run(os.getenv("TOKEN"))

#quack

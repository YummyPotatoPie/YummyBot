from discord.ext.commands import Context


class BotUtilites:

    @staticmethod
    def check_kick_permission(ctx: Context) -> bool:
        return ctx.author.top_role.permissions.kick_members

    @staticmethod
    def check_ban_permission(ctx: Context) -> bool:
        return ctx.author.top_role.permissions.ban_members

    @staticmethod
    def string_list_to_string(*strings: [str, ...]):
        result_string = ""
        for i in range(len(strings[0])):
            result_string += strings[0][i] + " "
        return result_string

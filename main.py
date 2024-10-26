import discord
from discord.ext import commands
from discord.commands import slash_command, SlashCommandGroup, Option
import requests
import re

bot = discord.Bot(intents=discord.Intents.all())
server_id = 
required_role_id = 

color_map = {
    "black": "0x080808",
    "white": "0xFFFFFF",
    "red": "0xFF0000",
    "green": "0x00FF00",
    "blue": "0x0000FF",
    "yellow": "0xFFFF00",
    "cyan": "0x00FFFF",
    "magenta": "0xFF00FF",
    "gray": "0x808080",
    "grey": "0x808080",
    "brown": "0xA52A2A",
    "orange": "0xFFA500",
    "pink": "0xFFC0CB",
    "purple": "0x800080",
    "teal": "0x008080",
    "maroon": "0x800000",
    "navy": "0x000080",
    "olive": "0x808000",
    "lime": "0x00FF00",
    "indigo": "0x4B0082",
    "turquoise": "0x40E0D0"
}

def get_emoji_url(text: str):
    if text.startswith("http") or text.startswith("https"):
        return text
    elif text.startswith("<:") or text.startswith("<a:") and text.endswith(">"):
        [first, _, third] = text.split(":")
        emojiId = third.replace(">", "")
        return f"https://cdn.discordapp.com/emojis/{emojiId}.png"
    elif "(" in text and ")" in text:
        url_match = re.search(r'\((.*?)\)', text)
        if url_match:
            return url_match.group(1)
    return None

@bot.event
async def on_ready():
    print(f"{bot.user.name}")

@bot.event
async def on_member_update(before, after):
    required_role = discord.utils.get(after.guild.roles, id=required_role_id)
    if required_role in before.roles and required_role not in after.roles:
        custom_role = next((role for role in after.guild.roles if role.name.startswith('‎ ') and role in after.roles), None)
        if custom_role:
            try:
                await custom_role.delete()
                print(f"Deleted Custom Role for {after.name}")
            except discord.Forbidden:
                print(f"Bot doesn't have permission to delete role for {after.name}")
                await after.send("I need permission to delete your custom role.")
            except Exception as e:
                print(f"Error while deleting role: {e}")
                await after.send("An unexpected error occurred while processing your request.")

class RoleCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    role = SlashCommandGroup("role", "Config Commands")

    @role.command(description='Update Role Name')
    async def name(self, ctx, parameter: Option(str, "Enter Name for the Role", required=True)):
        await ctx.response.defer(ephemeral=True)

        custom_role = next((role for role in ctx.author.roles if role.name.startswith('‎ ')), None)

        if custom_role:
            await custom_role.edit(name=f"‎ {parameter}", reason=f"Role Edit by {ctx.author.name}")
            embed = discord.Embed(description=f"Role Name Updated to {custom_role.name}", color=0x05ff72)
            await ctx.respond(embed=embed)
        else:
            role = await ctx.guild.create_role(name=f"‎ {parameter}", reason=f"VIP Role Creation by {ctx.author.name}")
            await role.edit(position=60)
            await ctx.author.add_roles(role)
            embed = discord.Embed(description=f"{role.name} Role Created for {ctx.author.name}", color=0x05ff72)
            await ctx.respond(embed=embed)

    @role.command(description='Add Colour to Role')
    async def colour(self, ctx, parameter: Option(str, "Enter Colour Name or HexColour for the Role", required=True)):
        await ctx.response.defer(ephemeral=True)

        parameter = parameter.lower().replace('#', '').replace('0x', '')
        if parameter in color_map:
            parameter = color_map[parameter]

        custom_role = next((role for role in ctx.author.roles if role.name.startswith('‎ ')), None)

        if custom_role:
            await custom_role.edit(color=int(parameter, 16), reason=f"Role Colour Edit by {ctx.author.name}")
            embed = discord.Embed(description=f"Role Colour Updated to #{parameter}", color=0x05ff72)
            await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(title="Please use `/role name` command first!", color=0x05ff72)
            await ctx.respond(embed=embed)

    @role.command(description="Add Icon to Custom Role")
    async def icon(self, ctx, parameter: Option(str, "Enter an Emoji", required=True)):
        await ctx.response.defer(ephemeral=True)

        custom_role = next((role for role in ctx.author.roles if role.name.startswith('‎ ')), None)

        if custom_role:
            try:
                url = get_emoji_url(parameter)
                if url is None:
                    await custom_role.edit(unicode_emoji=parameter)
                else:
                    response = requests.get(url)
                    data = response.content
                    await custom_role.edit(icon=data)
                embed = discord.Embed(description=f"Role Icon Updated Successfully", color=0x05ff72)
                await ctx.respond(embed=embed)
            except Exception as e:
                print(e)
                embed = discord.Embed(title="Error", color=0x05ff72)
                embed.set_footer(text="We could not update your icon. Message @kingpgc to fix it.")
                await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(title="Please use `/role name` command first!", color=0x05ff72)
            await ctx.respond(embed=embed)

bot.add_cog(RoleCommands(bot))

bot.run('')

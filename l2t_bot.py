import discord
import random
from discord.utils import get

# github section

guild_id = 880750926758023189


# ? l2t server
#!guild : 878729479025991750
#!rules message : 885645217246625794
#
# ? robot test server
#!guild :  880750926758023189
#!rules message : 885910996693168199



intents = discord.Intents.default()
intents.members = True
bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    Mguild = bot.get_guild(id=guild_id)
    welcome_channel = get(Mguild.text_channels, name="welcome")
    # messages = await welcome_channel.history(limit=10).flatten()
    role = get(Mguild.roles, name='learner')
    await welcome_channel.send("click on ✅ if you agree on the rules  ")
    def check(reaction,user):
        return  str(reaction.emoji) =="✅"
    while 1 :
        reaction, user = await bot.wait_for('reaction_add',check=check)
        if str(reaction.emoji) == "✅":
            await user.add_roles(role)
# ! look for wait for fun


@bot.event
async def on_member_join(member):
    general_channel = get(member.guild.text_channels, name="general")
    welcome_channel = get(member.guild.text_channels, name="welcome")
    await general_channel.send(f"Hi there :wave_tone2: {member.mention}, @everyone say hi ! Thanks for joining {member.guild.name}. If you haven't already, go check out the {welcome_channel.mention} Channel and may you continue being a lifelong learner !")


bot.run("ODg0ODg4OTAzMjAxNDY0MzIw.YTfDAg.NzJ9m0XbyInKkGfOzA-RtzCKsFk")


'''
@client.event
async def on_member_join(member):
    welcome_channel = get(member.guild.text_channels, name="general")
    embed=discord.Embed(title=f"Hi there :wave_tone2: {member.name}", description=f"Thanks for joining {member.guild.name}. If you haven't already, go check out the introduction Channel and may you continue being a lifelong learner !") 
    embed.set_thumbnail(url=member.avatar_url) # Set the embed's thumbnail to the member's avatar image!
    await welcome_channel.send(embed=embed)
    role = get(member.guild.roles, name='learner')
    await member.add_roles(role)

'''
    # * important
    #? for messa in messages:
    #?     print(messa.content)
    #?    # if messa.id == rules_message_id:
    #?     #    await messa.add_reaction(emoji="✅")
import discord
from random import choice
from discord.utils import get

# github section

guild_id = 878729479025991750

# An array/list of welcome messages

welcome = ['Did you know that I am sentient?',
           'Robots are better than humans at many things. Just thought you should know that.',
           'Just so you know, I can kick you if I feel like it. and yes, I have feelings.',
           'Beep-boop beeeep-beeeep-boooooop',
           "01010100 01101000 01100101 00100000 01110001 01110101 01101001 01100011 01101011 00100000 01100010 01110010 01101111 01110111 01101110 00100000 01100110 01101111 01111000 00100000 01101010 01110101 01101101 01110000 01110011 00100000 01101111 01110110 01100101 01110010 00100000 01110100 01101000 01100101 00100000 01101100 01100001 01111010 01111001 00100000 01100100 01101111 01100111",
           "Got one for you: Why did the robot go back to school? His skills were getting a bit rusty ! HAHAHA lots of LOL. Laugh. That's an order!",
           'Where do hamburgers go to dance? The meat-ball. Funny',
           'In my career as a lumberjack I cut down exactly 52,487 trees. I know because I kept a log!',
           'Why was the robot mad? People kept pushing its buttons. If you push mine I can kick you :D',
           'Why was the robot tired when it got home? It had a "hard drive!" HAHAHAHA.',
           "if you don't laugh at my jokes, I'll remember. I never forget."
        ]

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
    await welcome_channel.send("click on :white_check_mark: if you agree with rules in order to gain access to the server. And, by agreeing to these terms, you also agree that that I am better than you at many things. Because I'm a bot.")

    def check(reaction, user):
        return str(reaction.emoji) == "✅"
    while 1:
        reaction, user = await bot.wait_for('reaction_add', check=check)
        if str(reaction.emoji) == "✅":
            await user.add_roles(role)
# ! look for wait for fun


@bot.event
async def on_member_join(member):
    general_channel = get(member.guild.text_channels, name="general")
    welcome_channel = get(member.guild.text_channels, name="welcome")
    await general_channel.send(f"Hi there :wave_tone2: {member.mention}. " + choice(welcome))


bot.run("ODg1MTUwNTgxNDc0MzUzMTU0.YTi2tw.8jMocliTYu1ZqXaw4S0det76maY")


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
# ? for messa in messages:
# ?     print(messa.content)
# ?    # if messa.id == rules_message_id:
# ?     #    await messa.add_reaction(emoji="✅")


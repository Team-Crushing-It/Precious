import discord
from random import choice
from discord.utils import get

# defining the guild id (server id) we'll use it later
guild_id = 878729479025991750
# defining the rules message we'll use it later
rules_message_id = 885645217246625794
# An array/list of welcome messages

# this is a list of all the the responds that precious
# could generate 
# we made it to send a random "funny" message 
# when someone joins the server
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
# here we are getting the default intents (permissions) that 
# discord api gives you
# from discord API docs
# default()
# A factory method that creates a Intents with everything enabled except presences and members.
# https://discordpy.readthedocs.io/en/stable/api.html#discord.Intents.default
intents = discord.Intents.default()
# here we are enabling the member intent bcs it's disabled
# when using default
intents.members = True
# here we are telling the bot to use these permissions (intents)
# and we are initializing the bot
# from discord api : 
# discord.Client
# Represents a client connection that connects to Discord.
bot = discord.Client(intents=intents)

# this function is called when the bot joins 
# the server for the first time
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    # here we are specifying the guild id 
    # bcs we need to get a specific msg(rules message)
    # and when someone click the checks the green mark emoji 
    # precious gives him the learner role wich allow him to acces the server
    Mguild = bot.get_guild(id=guild_id)
    # here we are getting the channel that contains rules (welcome channel) by it's name
    welcome_channel = get(Mguild.text_channels, name="welcome")
    # here we are getting the history to get the message that contains rules in the welcome 
    # channel , to do so we fetched the history of the channel
    # if you wondering what flatter() does :
    # it Flattens the async iterator into a list with all the elements
    #  https://discordpy.readthedocs.io/en/stable/api.html?highlight=flatten#discord.AsyncIterator.flatten
    # for more info : 
    # https://stackoverflow.com/questions/63863871/discord-py-how-to-go-through-channel-history-and-search-for-a-specific-message
    messages = await welcome_channel.history(limit=10).flatten()
    # now that we got the 10 last messages in limit of 10 
    # we are getting the first element [0] because the rules message in the welcome 
    # is the first one this syntax is called list comprehension 
    # for more info : https://www.geeksforgeeks.org/python-list-comprehension/
    rules_message =  [i for i in messages if i.id == rules_message_id][0]
    # here we are adding a reaction from the bot (we've been trying to test if on_raw_reaction_add is working)
    await rules_message.add_reaction( emoji='✅')

# Called when a message has a reaction added
# https://discordpy.readthedocs.io/en/stable/api.html?highlight=on_raw_reaction_add#discord.on_raw_reaction_add
@bot.event
async def on_raw_reaction_add(payload):
    # here we are getting the L2T server
    # it maybe a bad practice but we are using precious only in L2T server
    Mguild = bot.get_guild(id=guild_id)
    # here we are getting the channel that contains rules (welcome channel) by it's name
    Channel = get(Mguild.text_channels, name="welcome")
    # we are checking if the emoji is ✅ and the message that got the emoji is the rules message
    # and the the channel is the welcom channel
    if payload.emoji.name == "✅" and payload.message_id == rules_message_id and payload.channel_id == Channel.id:
      # here we are getting the learner role which gives the user access
      Role = get(Mguild.roles, name="learner")
      # here we are giving the learner role to the user that reacted with ✅ 
      await payload.member.add_roles(Role)
# Called when a member joins the server
@bot.event
async def on_member_join(member):
    # here we are getting the general channel to say hi to the new member and tell him a "joke"
    general_channel = get(member.guild.text_channels, name="general")
    # no need of this but we don't what to delete anything we are afraid of breaking the code :) 
    welcome_channel = get(member.guild.text_channels, name="welcome")
    # here we are sending a message that welcomes the use and tells him a random "joke" 
    # using the choice function , this functions gets a random item from the welcome list(which contains jokes)
    await general_channel.send(f"Hi there :wave_tone2: {member.mention}. " + choice(welcome))

# here we are running the bot and telling the API which bot we are using
bot.run("ODg0ODg4OTAzMjAxNDY0MzIw.YTfDAg.46XLFQWRJHe9z5fPbGB9dzS7fCc")

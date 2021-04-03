import discord
import os
import random
from discord import *
from discord.ext import commands
import requests
import sys
import subprocess
import os
import time
from time import sleep
from discord import ext
from os import system
from discord import User
from discord.ext.commands import Bot, guild_only
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext import *
from discord.ext.commands import *
from discord import *
from discord.ext import tasks
import asyncio
import time
from itertools import cycle
import emoji
status = cycle(['.help ', '.help (super straight is small dick energy )', '.help (lgbtqia+ is  da best)',  '.help (i have a big ass big boobs and i like to eat pussy', '.help (jaming nicki minaj)', '.help (any pronounce)', '.help (no racism please)', '.help (GIVE ME BUSSY NO SHORT DICK)' '.help (BITCH I AM A LESSBIAN)', '.help (i am the owner now)', '.help (TRANS RIGHTS)', '.help (BLACK LIVES MATTER)', '.help (FUCK TRUMP)', '.help (YAAASS QUEEN YOU SLAYING)', '.help (can anyone play chess?? )'])  
e = discord.Embed()
client = commands.Bot(command_prefix='.', help_command=None)
@client.event
async def on_ready():
    os.system('cls')
    print('Bot is ready.')
    update_status.start()
    channel = client.get_channel(801723466394107915)
    await channel.send('hello')
    emoji = '\N{THUMBS UP SIGN}'
    await message.add_reaction(emoji)

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
       await member.ban(reason=reason)
       await ctx.send(f'Banned nicki minaj destroyed your carrier')
@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
         banned_users = await ctx.guild.bans()
         member_name, member_discriminator = member.split('#')
     
         for ban_entry in banned_users:
             user = ban_entry.user
         
             if (user.name, user.discriminator) == (member_name, member_discriminator):
                 await ctx.guild.unban(user)
                 await ctx.send(f'Unbanned {user.name}#{user.discriminator} nicki minaj restored your carrier')
                 return
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
  await user.kick(reason=reason)
  await ctx.send(f"{user}s carrier has been ended sucessfully (for a little bit)")
  
  
@client.command()
async def ping(ctx):
    await ctx.send(f"pong {round(client.latency * 1000)}ms")
    
@client.command()
async def help(ctx):
    embed=discord.Embed(title=".help", description="this is a help command", color=0xff0000)
    embed.set_thumbnail(url="https://image.flaticon.com/icons/png/512/682/682055.png")
    embed.add_field(name=".ban", value="NICKI MINAJJJJ bans an user", inline=False)
    embed.add_field(name=".kick", value="NICKI MINAJJJJ kicks an user", inline=False)
    embed.add_field(name=".unban", value="NICKI MINAJJJJ unbans an user", inline=False)
    embed.add_field(name=".nickiminaj", value="BARB OWERLOAD", inline=False)
    embed.add_field(name=".mute", value="NICKI MINAJJJJ Mutes a member", inline=False)
    embed.add_field(name=".unmute", value="NICKI MINAJJJJ Unmutes a member", inline=False)
    embed.add_field(name=".clear", value="NICKI MINAJJJJ clears the evedence (messages)", inline=False)
    embed.add_field(name="pride flags", value="example: .gay (shows a pride flag)", inline=False)    
    embed.add_field(name=".exit", value="taskkills the bot", inline=False)    
    embed.set_footer(text="dis is a help command if you didnt get it bitch", )
    await ctx.send(embed=embed)
    
@client.command()
async def nickiminaj(ctx):
    await ctx.send(f"nicki minaj is the queen of rap :sparkles: ")
    time.sleep(0.3)
    await ctx.send(f"nicki minaj is the queen of rap :sparkles: ")
    time.sleep(0.3)
    await ctx.send(f"nicki minaj is the queen of rap :sparkles: ")
    time.sleep(0.3)
    await ctx.send(f"nicki minaj is the queen of rap :sparkles: ")
    time.sleep(0.3)
    await ctx.send(f"nicki minaj is the queen of rap :sparkles: ")
    time.sleep(0.3)
    await ctx.send(f"nicki minaj is the queen of rap :sparkles: ")
    time.sleep(0.3)
    await ctx.send(f"https://static.billboard.com/files/media/nicki-minaj-award-mtv-vma-2015-show-billboard-650-compressed.jpg")

@tasks.loop(seconds=10)
async def update_status():
    await client.change_presence(activity=discord.Game(next(status)))
@client.command(description="Mutes the specified user.")
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")
@client.command(description="Unmutes a specified user.")
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" you have unmutedd from: - {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)
@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=30):
    await ctx.channel.purge(limit=amount)
@client.command()
@commands.has_permissions(administrator=True)
async def exit(ctx):
    await ctx.channel.send(f"bot is being exited")
    os.system('taskkill /im python.exe /f')
@client.command()
async def gay(ctx):
    await ctx.channel.send(f"https://i1.wp.com/cadehildreth.com/wp-content/uploads/2020/12/Gay-Men-Pride-Flag.png?resize=506%2C304&ssl=1")
    await ctx.channel.send(f"Gay refers to the attraction towards or desire for the same gender (or similar genders to one's own). Terms such as homosexual and homoromantic can be considered synonyms or subcategories of the gay umbrella. While gay applies to men, women, and non-binary people, it is sometimes used to only refer to gay men.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def bisexual(ctx):
    await ctx.channel.send(f"https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Bisexual_Pride_Flag.svg/800px-Bisexual_Pride_Flag.svg.png")
    await ctx.channel.send(f"Bisexual (often shortened to Bi) refers to someone who is attracted to two or more genders. It is also sometimes worded as the attraction to genders both the same as and different than one's own. This is most commonly understood to mean men and women, although bisexual activists have been outspoken about the fact that it is not limited to the gender binary.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def bi(ctx):
    await ctx.channel.send(f"https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Bisexual_Pride_Flag.svg/800px-Bisexual_Pride_Flag.svg.png")
    await ctx.channel.send(f"Bisexual (often shortened to Bi) refers to someone who is attracted to two or more genders. It is also sometimes worded as the attraction to genders both the same as and different than one's own. This is most commonly understood to mean men and women, although bisexual activists have been outspoken about the fact that it is not limited to the gender binary.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def asexual(ctx):
    await ctx.channel.send(f"https://www.crwflags.com/fotw/images/q/qq-asex.gif")
    await ctx.channel.send(f"Asexuality is a part of the asexual spectrum, and is defined by a lack of sexual attraction. Asexual experiences may also include: not wanting to have sex, not being interested in sex, not experiencing a sex drive/libido, or being repulsed by sex.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def ace(ctx):
    await ctx.channel.send(f"https://www.crwflags.com/fotw/images/q/qq-asex.gif")
    await ctx.channel.send(f"Asexuality is a part of the asexual spectrum, and is defined by a lack of sexual attraction. Asexual experiences may also include: not wanting to have sex, not being interested in sex, not experiencing a sex drive/libido, or being repulsed by sex.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def aromantic(ctx):
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/2/2a/Aroflag.jpg/revision/latest?cb=20180701010015")
    await ctx.channel.send(f"Aromantic (often shortened to aro) means someone who generally does not experience romantic attraction. Romantic attraction is defined as the desire to be in a romantic relationship and/or do romantic acts with a specific person.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def aro(ctx):
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/2/2a/Aroflag.jpg/revision/latest?cb=20180701010015")
    await ctx.channel.send(f"Aromantic (often shortened to aro) means someone who generally does not experience romantic attraction. Romantic attraction is defined as the desire to be in a romantic relationship and/or do romantic acts with a specific person.")
    await ctx.channel.send(f"WE LOVE YOU") 
@client.command()
async def greysexual(ctx):
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/1/1d/Greysexual.png/revision/latest/scale-to-width-down/220?cb=20200706032353")
    await ctx.channel.send(f"Greysexual or Greyasexual, also spelled Graysexual or Grayasexual (shortened to Grey Ace or Grace) is a sexual orientation on the asexual spectrum, referring to those who relate to asexuality, yet feel that there are parts of their experience that aren't fully described by the word asexual. Greysexual can be used as a specific identity, or as an umbrella term for any ace-spec identity that isn't purely asexual, including demisexual and others. A common reason someone may identify as greysexual is that they experience sexual attraction but very infrequently. Some greysexual people may only feel sexual attraction once or twice in their life. Others may experience it more frequently, but still not as frequently as allosexual people.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def greyromantic(ctx):
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/6/68/Grayaroflag.png/revision/latest/scale-to-width-down/220?cb=20180701140158")
    await ctx.channel.send(f"Greyromantic or Greyaromantic (also spelled as Grayromantic or Grayaromantic) is a romantic orientation on the aromantic spectrum which describes those who relate with aromanticism, yet feel that there are parts of their experience that aren't fully described by the word aromantic. Greyromantic can be used as a specific identity, or as an umbrella term for any aro-spec identity that isn't purely aromantic, including demiromantic and others. A common reason someone may identify as greyromantic is that they experience romantic attraction but very infrequently. Some greyromantic people may only feel romantic attraction once or twice in their life. Others may experience it more frequently, but still not as frequently as alloromantic people.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def demisexual(ctx):
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/8/86/Demiflag.png/revision/latest/scale-to-width-down/220?cb=20180701203456")
    await ctx.channel.send(f"Demisexual is a sexual orientation on the asexual spectrum defined as someone who does not experience sexual attraction until they have formed a deep emotional connection with someone. The connection can be romantic, platonic, or some other form of connection. What counts as a close connection can vary between demisexuals. Forming an emotional bond with someone does not mean that one is automatically attracted to said person, as it just means there's now a possibility for one to feel attraction.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def demiromantic(ctx):
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/1/15/Demiaroflag.png/revision/latest/scale-to-width-down/220?cb=20180701134752")
    await ctx.channel.send(f"Demiromantic is a romantic orientation on the aromantic spectrum defined as someone who does not experience romantic attraction until they have formed a deep emotional connection with someone. The connection can be sexual, platonic, or some other form of connection. Forming an emotional bond with someone does not mean that one is automatically attracted to said person, as it just means there's now a possibility for one to feel attraction.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def trans(ctx):
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/c/cd/Transgender.png/revision/latest/scale-to-width-down/220?cb=20180704133930")
    await ctx.channel.send(f"Transgender (often shortened to trans) is a term referring to people who do not identify as the gender assigned to them at birth. It commonly refers to men who were assigned female at birth (trans men), and women who were assigned male at birth (trans women), these examples being known as binary trans people. All non-binary people are also inherently included under the term trans, because their gender is not what was assigned to them at birth. Although, some non-binary people choose not to identify as trans.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def transgender(ctx):
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/c/cd/Transgender.png/revision/latest/scale-to-width-down/220?cb=20180704133930")
    await ctx.channel.send(f"Transgender (often shortened to trans) is a term referring to people who do not identify as the gender assigned to them at birth. It commonly refers to men who were assigned female at birth (trans men), and women who were assigned male at birth (trans women), these examples being known as binary trans people. All non-binary people are also inherently included under the term trans, because their gender is not what was assigned to them at birth. Although, some non-binary people choose not to identify as trans.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def genderfluid(ctx):
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/2/2a/Genderfluidflag.jpg/revision/latest/scale-to-width-down/220?cb=20180716213954")
    await ctx.channel.send(f"Genderfluid refers to someone whose gender identity changes over time. A genderfluid person can identify as any gender, or combination of genders at any given time. Their gender can change at random or it may vary in response to different circumstances. One's gender can change over the course of hours, days, weeks, months, or years. For some people their gender changes on a somewhat consistent schedule, for others their gender changes at random times. Some genderfluid people can be fluid between all genders, or a large amount of genders. Other genderfluid people are fluid between a small handful of genders.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def pansexual(ctx):
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/3/30/Panflag.png/revision/latest/scale-to-width-down/259?cb=20180703173642")
    await ctx.channel.send(f"Pansexual (often shortened to pan) is the attraction to people regardless of gender. As a result, they are attracted to all genders. Pansexual people may be described as being gender blind showing that gender is not a factor in their attraction to a person.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def pan(ctx):
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/3/30/Panflag.png/revision/latest/scale-to-width-down/259?cb=20180703173642")
    await ctx.channel.send(f"Pansexual (often shortened to pan) is the attraction to people regardless of gender. As a result, they are attracted to all genders. Pansexual people may be described as being gender blind showing that gender is not a factor in their attraction to a person.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def genderqueer(ctx):
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/e/e0/Genderqueerflag.png/revision/latest/scale-to-width-down/220?cb=20180716205859")
    await ctx.channel.send(f"Genderqueer is a term for people who feel that they have a queer or non-normative experience with gender, either through their gender identity, their gender presentation, or other experiences of gender. It is often used interchangeably with non-binary to mean a gender that is not strictly male or female. This definition can be used as a gender identity on its own or as an umbrella term.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def nb(ctx):
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/f/f2/Enbyflag.png/revision/latest/scale-to-width-down/220?cb=20180704140834")
    await ctx.channel.send(f"Non-Binary (sometimes shortened to NB or enby) refers to someone whose gender does not fall strictly within the category of the binary genders (man or woman) that are used in western society. Anyone who is not always, solely, 100% male or female can be considered non-binary. Some non-binary people may identify with one or both of the binary genders, at least in part. Non-binary can be a gender identity on its own, or it can be used as an umbrella term for anyone whose gender is something other than male or female. Some people may also use the term genderqueer interchangeably with non-binary.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def enby(ctx):
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/f/f2/Enbyflag.png/revision/latest/scale-to-width-down/220?cb=20180704140834")
    await ctx.channel.send(f"Non-Binary (sometimes shortened to NB or enby) refers to someone whose gender does not fall strictly within the category of the binary genders (man or woman) that are used in western society. Anyone who is not always, solely, 100% male or female can be considered non-binary. Some non-binary people may identify with one or both of the binary genders, at least in part. Non-binary can be a gender identity on its own, or it can be used as an umbrella term for anyone whose gender is something other than male or female. Some people may also use the term genderqueer interchangeably with non-binary.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def nonbinary(ctx):
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/f/f2/Enbyflag.png/revision/latest/scale-to-width-down/220?cb=20180704140834")
    await ctx.channel.send(f"Non-Binary (sometimes shortened to NB or enby) refers to someone whose gender does not fall strictly within the category of the binary genders (man or woman) that are used in western society. Anyone who is not always, solely, 100% male or female can be considered non-binary. Some non-binary people may identify with one or both of the binary genders, at least in part. Non-binary can be a gender identity on its own, or it can be used as an umbrella term for anyone whose gender is something other than male or female. Some people may also use the term genderqueer interchangeably with non-binary.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def intersex(ctx):
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/3/32/Intersexflag.jpg/revision/latest/scale-to-width-down/220?cb=20180716194619")
    await ctx.channel.send(f"Intersex is a term for those born with physical sex characteristics that cannot be traditionally classified as male or female. Variations may appear in a person’s chromosomes, natural hormones, genitalia, or gonads, secondary sex characteristics, or some combination of these things. Intersexuality is observed in many animals including humans. According to the ISNA it is estimated that as many as 1.7% of people are born with intersex traits.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def lesbian(ctx):
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/4/47/Lesbian_flag.jpg/revision/latest/scale-to-width-down/310?cb=20200428020201")
    await ctx.channel.send(f"Lesbian is the term for a gay woman, meaning a woman, woman-aligned and/or feminine-aligned non-binary person who is attracted to women, woman-aligned and/or feminine-aligned non-binary people. The term is also sometimes used by abinary non-binary people who are attracted to women, women-aligned people, feminine aligned people, and other non-binary people who identify as lesbians. Some people use it as the feminine equivalent of vincian (referring to exclusive attraction).")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def polysexual(ctx):
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/6/67/Polysexualflag.png/revision/latest/scale-to-width-down/310?cb=20180703180155")
    await ctx.channel.send(f"Polysexuality, also spelled plysexuality or polisexuality, is the sexual attraction to many, but not necessarily all, genders. For example, a polysexual person could be attracted to all genders except men, or a polysexual person could be attracted only to non-binary people, genderfluid people, and male-aligned people. Polysexual general implies that one is attracted to more than two genders, but one can be any number of genders anywhere between two genders to all genders besides one. Polysexual people may or may not have a preference and may or may not experience a difference between genders.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def polyamorous(ctx):
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/5/53/Polyflag.png/revision/latest/scale-to-width-down/220?cb=20180703181920")
    await ctx.channel.send(f"Polyamory is the capability or desire to be in a relationship with more than one person at once. Polyamorous can be used both as a description of a relationship with more than two people and as description of people who desire such relationships. Polyamorous relationships can be romantic, sexual, or both; they may also be based on tertiary attraction such as queerplatonic relationships. Polyamory is not considered cheating, because all parties are aware of all other parties involved and consent to their involvement. Polyamory can be as simple as an open relationship or it can be three or more people who are all in a relationship with each other. Polyamorous is not a sexuality on its own, but more of a description of how one can experience attraction. Polyamorous people can have any sexuality.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def superstraight(ctx):
    await ctx.channel.send(f"YOU FUCKING BITCH")
    time.sleep(0.5)
    await ctx.channel.send(f"YOU FUCKING TRANSPHOBE")
    time.sleep(0.5)
    await ctx.channel.send(f"YOUR DUMB FUCKING ASS IS GETTING KICKED")
    time.sleep(0.5)
    await ctx.channel.send(f"THE WHOLE LGBTQIA+ HATES YOU")
    time.sleep(0.5)
    await ctx.channel.send(f"WE ALL FUCKING HATE YOU")
    time.sleep(0.5)
    await ctx.channel.send(f"WE ALL FUCKING HATE YOU")
    time.sleep(0.5)
    await ctx.channel.send(f"WE ALL FUCKING HATE YOU")
    time.sleep(0.5)
    await ctx.channel.send(f"WE ALL FUCKING HATE YOU")
    time.sleep(0.5)
    await ctx.channel.send(f"WE ALL FUCKING HATE YOU")
    time.sleep(0.5)
    await ctx.channel.send(f"@everyone")
    time.sleep(0.1)
    await ctx.channel.send(f"@everyone")
    time.sleep(0.1)
    await ctx.channel.send(f"@everyone")
    time.sleep(0.1)
    await ctx.channel.send(f"@everyone")
    time.sleep(0.1)
    await ctx.channel.send(f"@everyone")
    await ctx.channel.send(f":fire: :fire: :fire:   :black_large_square: :black_large_square: :black_large_square: ")
    await ctx.channel.send(f":orange_square: :orange_square: :orange_square:  :black_large_square: :black_large_square: :fire: ")
    await ctx.channel.send(f":orange_square: :orange_square: :orange_square:  :black_large_square: :fire: :fire: ")
    await ctx.channel.send(f":orange_square: :orange_square: :orange_square:  :fire: :fire: :fire: ")
    await ctx.channel.send(f":orange_square: :orange_square: :fire: :fire:  :fire: :fire:")
    await ctx.channel.send(f"AND YOU FUCKING CHOSE PORNHUB AND GRINDER COLORS F HDKJFGKGVKGVJKGJKGDFGJ")
    await ctx.channel.send(f"AND YOU CHOSE THE MONTH SEPTEMBER? MY OWNER IS A SEPTEMBER LIBRA AND AGREES TO FUCKING DELETE THAT MONTH")
    await ctx.channel.send(f"FUCK YOU ALL!! #KILLALLSS FUCK YOU ALLLLLLLLLLLLLLLLL")
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/0/0c/Transgender_symbol.png/revision/latest/scale-to-width-down/180?cb=20201217015207")
@client.command()
async def ss(ctx):
    await ctx.channel.send(f"YOU FUCKING BITCH")
    time.sleep(0.5)
    await ctx.channel.send(f"YOU FUCKING TRANSPHOBE")
    time.sleep(0.5)
    await ctx.channel.send(f"YOUR DUMB FUCKING ASS IS GETTING KICKED")
    time.sleep(0.5)
    await ctx.channel.send(f"THE WHOLE LGBTQIA+ HATES YOU")
    time.sleep(0.5)
    await ctx.channel.send(f"WE ALL FUCKING HATE YOU")
    time.sleep(0.5)
    await ctx.channel.send(f"WE ALL FUCKING HATE YOU")
    time.sleep(0.5)
    await ctx.channel.send(f"WE ALL FUCKING HATE YOU")
    time.sleep(0.5)
    await ctx.channel.send(f"WE ALL FUCKING HATE YOU")
    time.sleep(0.5)
    await ctx.channel.send(f"WE ALL FUCKING HATE YOU")
    time.sleep(0.5)
    await ctx.channel.send(f"@everyone")
    time.sleep(0.1)
    await ctx.channel.send(f"@everyone")
    time.sleep(0.1)
    await ctx.channel.send(f"@everyone")
    time.sleep(0.1)
    await ctx.channel.send(f"@everyone")
    time.sleep(0.1)
    await ctx.channel.send(f"@everyone")
    await ctx.channel.send(f":fire: :fire: :fire:   :black_large_square: :black_large_square: :black_large_square: ")
    await ctx.channel.send(f":orange_square: :orange_square: :orange_square:  :black_large_square: :black_large_square: :fire: ")
    await ctx.channel.send(f":orange_square: :orange_square: :orange_square:  :black_large_square: :fire: :fire: ")
    await ctx.channel.send(f":orange_square: :orange_square: :orange_square:  :fire: :fire: :fire: ")
    await ctx.channel.send(f":orange_square: :orange_square: :fire: :fire:  :fire: :fire:")
    await ctx.channel.send(f"AND YOU FUCKING CHOSE PORNHUB AND GRINDER COLORS F HDKJFGKGVKGVJKGJKGDFGJ")
    await ctx.channel.send(f"AND YOU CHOSE THE MONTH SEPTEMBER? MY OWNER IS A SEPTEMBER LIBRA AND AGREES TO FUCKING DELETE THAT MONTH")
    await ctx.channel.send(f"FUCK YOU ALL!! #KILLALLSS FUCK YOU ALLLLLLLLLLLLLLLLL")
    await ctx.channel.send(f"https://static.wikia.nocookie.net/lgbta/images/0/0c/Transgender_symbol.png/revision/latest/scale-to-width-down/180?cb=20201217015207")
@client.command()
async def demiboy(ctx):
    await ctx.channel.send(f"https://static.wikia.nocookie.net/gender/images/3/34/Demiboyflag.png/revision/latest/scale-to-width-down/220?cb=20161228065614")
    await ctx.channel.send(f"A demiboy (also called a demiguy, demiman or demimale person) is a gender identity describing someone who partially, but not wholly, identifies as a man, boy or otherwise masculine, regardless of their assigned gender at birth. They may or may not identify as another gender in addition to feeling partially a boy or man. Demiboy can be used to describe someone assigned male at birth who feels barely connected or disconnected to that identification, but who usually does not experience a significant enough dissociation to create real physical discomfort or dysphoria.")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def agender(ctx):
    await ctx.channel.send(f"https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Agender_pride_flag.svg/143px-Agender_pride_flag.svg.png")
    await ctx.channel.send(f"Non-binary (also spelled nonbinary) or genderqueer is a spectrum of gender identities that are not exclusively masculine or feminine‍—‌identities that are outside the gender binary. Non-binary identities can fall under the transgender umbrella, since many non-binary people identify with a gender that is different from their assigned sex. Another term for non-binary is enby (from the abbreviation 'NB'). Non-binary people may identify as having two or more genders (being bigender or trigender); having no gender (agender, nongendered, genderless, genderfree or neutrois); moving between genders or having a fluctuating gender identity (genderfluid); being third gender or other-gendered (a category that includes those who do not place a name to their gender).")
    await ctx.channel.send(f"WE LOVE YOU")
@client.command()
async def warn(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    warnedRole = discord.utils.get(guild.roles, name="warned")

    if not warnedRole:
        warnedRole = await guild.create_role(name="warned")

        for channel in guild.channels:
            await channel.set_permissions(warnedRole, speak=True, send_messages=True, read_message_history=True, read_messages=True)
    embed = discord.Embed(title="warned", description=f"{member.mention} was warned ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(warnedRole, reason=reason)
    await member.send(f" you have been warned from: {guild.name} reason: {reason}")
@client.event
async def on_reaction_add(reaction, user):
  ChID = '801723466394107915'
  if reaction.message.channel.id != ChID:
    return
  if reaction.emoji == "emoji":
    muted = discord.utils.get(user.server.roles, name="muted")
    await client.add_roles(user, muted)
client.run('#INSERT YOUR TOKEN HERE#')




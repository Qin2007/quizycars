import itertools
import json
from math import floor as down
from time import time as now

import disnake
from disnake.ext import commands

# change
SUPPORT_SERVER_INVITELINK = ''  # here is your chance to promote your server
addto_question_number_quiz1 = 0  # adds to the value shown to the user
addto_question_number_quiz2 = 0  # adds to the value shown to the user
intents = disnake.Intents(dm_messages=False, message_content=False, guild_messages=False, guilds=True)
ibot = commands.InteractionBot(intents=intents)
helpm = """howdy mate
im there your fave quizy mate
you know im quizy ant
use the /resume command to start or resume the main quiz,
/setquestion and getquestion are to get and set a user generated question
/rmquestion is to remove it
this is chapter 2
"""
quizyant1 = disnake.utils.oauth_url(
    1014958581814141039, permissions=disnake.Permissions(117760),
    scopes=('bot', 'applications.commands')
)  # marks the first quizy ant
quizyant2 = disnake.utils.oauth_url(
    1020976399122714675, permissions=disnake.Permissions(117760),
    scopes=('bot', 'applications.commands')
)  # marks the second quizy ant
linkz = [
    ['stuck on the question?', ],
    ['github for base', 'https://github.com/Qin2007/quizyantBase/settings'],
    ['authorizer link quizyant1', quizyant1],
    ['car7002', 'https://discord.com/users/894198592670158898'],
    ['authorizer link quizyant2', quizyant2],
    ['original bot support', 'https://discord.gg/ScHpx3YKDx']
]  # links used on the help command; ['LINK NAME','LINK URL']
token = ''  # token here
SUPPORTS_A_SECOND_QUIZ = False
userbase = {
    'int': 1,
    'exp': 0,
    'qint': 0,
    'lives': 5,  # this is how many lives the player has in the first quiz
    'skips': 1,  # this is how many skips the player has in the first quiz

    'int2': 1,
    'lives2': 3,  # this is how many lives the player has in the second quiz
    'skips2': 1,  # this is how many skips the player has in the second quiz
}

emojiz = {
    'skip': 'skiP()',
    'bombofLives': 'Livez()',
    'bnone': 'L()',
    'loaded1': '<:load1:1010230456807084062>',
    'loaded2': '<:load2:1010230460783284254>',
    'loaded3': '<:load3:1010230453464215733>',
    'un1': '<:un1:1010230459126517760>',
    'un2': '<:un2:1010230462263861259>',
    'un3': '<:un3:1010230455255191632>',
    'RedNo': '<:RedNo:1005394297719357461>',
    'GreenYes': '<:GreenYes:1005394250088841266>',
}  # the default emojis, if they cant load

followups = [
    disnake.OptionChoice(
        name='announcements',
        value='1012013349204148264'
    ),
    disnake.OptionChoice(
        name='update log',
        value='1012013273647956110'
    ),
    # you can add mmore channels, but the code is build on this format
    #     disnake.OptionChoice(
    #         name='update log', # the name, shows to he user
    #         value='1012013273647956110' # the channel id, in string
    #     ),
]


def getemojis():
    global emojiz
    discord = disnake
    client = ibot
    # guild = client.get_guild(943489205546401842).emojis
    botz = client.get_guild(951768916030533662).emojis
    # this guild id is bot support; invite http://discord.gg/7jTVq6qbm6
    emojiz = {
        # 1: discord.utils.find(lambda m: m.name == 'BotDislike', guild),
        # 2: discord.utils.find(lambda m: m.name == 'slash', guild),
        # 3: discord.utils.find(lambda m: m.name == 'BotLike', guild),
        # 'crown': discord.utils.find(lambda m: m.name == 'the_crown', botz),
        # 'ivote': discord.utils.find(lambda m: m.name == 'ivote', botz),
        'skip': discord.utils.find(lambda m: m.name == 'bombskip', botz),  # the emoji of the skip
        'bombofLives': discord.utils.find(lambda m: m.name == 'bombofLives', botz),  # the emoji for lives

        'bnone': discord.utils.find(lambda m: m.name == 'bnone', botz),  # if a slot isempty this will be used
        # emojis below are not used
        'loaded1': '<:load1:1010230456807084062>',
        'loaded2': '<:load2:1010230460783284254>',
        'loaded3': '<:load3:1010230453464215733>',
        'un1': '<:un1:1010230459126517760>',
        'un2': '<:un2:1010230462263861259>',
        'un3': '<:un3:1010230455255191632>',
        'RedNo': '<:RedNo:1005394297719357461>',
        'GreenYes': '<:GreenYes:1005394250088841266>',
    }
    pass


whichquizy2 = [
    # the name= is the name of the quiz, the value= should not be changed
    disnake.OptionChoice(name='MAiN quiz', value='quiz 2'),
    disnake.OptionChoice(name='secondary quiz', value='quiz 3'),
]
with open('', 'r') as f:  # path in the '
    pool = json.load(f)
if SUPPORTS_A_SECOND_QUIZ:
    with open('', 'r') as f:  # path in the
        pool2 = json.load(f)
# stop changing

on_linux = True  # marks the test version

cooldowns = {}


# this function is useless, if it returns true the command cant run, else the command runs as normal
async def ismemberbanned(inter, memberid):
    # if memberid in banned_members:
    #     await inter.send(
    #         content=defmemberbanmessage, components=[
    #             disnake.ui.Button(
    #                 style=disnake.ButtonStyle.link, label='ban appeals',
    #                 url=docsgoogle
    #             )
    #         ],
    #         ephemeral=True
    #     )
    #     return True
    # else:
    #     return False
    return False


qcount = itertools.count(start=1)  # an integer?

members = {}
pass
recurring_asnwers = {
    'thisone': ["Was it this one?", "This one?", "Maybe this one!", "...or this one?"],
    'outoforder': ["out of order", "out of order", "out of order", "out of order", "out of order"],
    'choose': ["choose", "choose", "choose", "choose", ]
}
qs = len(pool)

pass
if SUPPORTS_A_SECOND_QUIZ:
    qs2 = len(pool2)
maxips = userbase['skips']
if SUPPORTS_A_SECOND_QUIZ:
    maxips2 = userbase['skips2']
    for gv in pool2.values():
        gii = gv.get('getaskip', 0)
        maxips2 += gii


def gradembed(inter: disnake.Interaction, embed: disnake.Embed,
              gradeintoverwrite: int = None, quiz=1) -> disnake.Embed:
    if quiz == 1:
        gradeint = members[inter.author.id]['lives'] - 1  # 4 max 0 min
        gradeint += members[inter.author.id]['skips']  # 10 max 0 min # +6 max # 0 min
        maxinty = userbase['skips'] + (userbase['lives'] - 1)
        if gradeintoverwrite > maxinty:
            gradeint = maxinty
        elif gradeintoverwrite:
            gradeint = gradeintoverwrite
        gradestr = 'grade! (quiz 1)'
    elif quiz == 2:
        gradeint = members[inter.author.id]['lives2'] - 1
        gradeint += members[inter.author.id]['skips2']
        maxinty = userbase['skips2'] + (userbase['lives2'] - 1)
        if gradeintoverwrite > maxinty:
            gradeint = maxinty
        elif gradeintoverwrite:
            gradeint = gradeintoverwrite
        gradestr = 'grade! (quiz 1)'
    else:
        gradestr = 'error!'
        gradeint = '`Error!`'
        maxinty = gradeint
    embed.add_field(name=gradestr, value=f'you have a score of {gradeint} out of {maxinty}')
    return embed


async def cantrun(inter, cooldint: int, fromm: str) -> tuple[bool, disnake.Guild]:  # cooldowns
    guild: disnake.Guild = inter.guild
    thenow = down(now())
    if not cooldowns.get(guild.id):
        cooldowns[guild.id] = {}

    if not cooldowns[guild.id].get(fromm):
        cooldowns[guild.id][fromm] = thenow - cooldint - 1

    if thenow - cooldowns[guild.id][fromm] >= cooldint:
        cooldowns[guild.id][fromm] = thenow
    else:
        await inter.send(f'cooldown, try again <t:{thenow + cooldint}:R>', ephemeral=True)
        return True, guild
    return False, guild


async def gotitright(authorid, isstory, quizyint):
    userid = authorid
    if isstory:
        if not members.get(userid):
            members[userid] = userbase.copy()
        if quizyint == 2:
            members[authorid]['int2'] += 1
        elif quizyint == 1:
            members[authorid]['int'] += 1
        members[authorid]['exp'] += 25


def pnametointc(pname: str, pnameonce: str, integer: int, secondarycharacter: str) -> str:
    # return str(pname) + str(str(secondarycharacter) * int(((integer * len(pname)) / len(pname)) - len(pname)))
    pcount = pname.count(pnameonce)
    if not (14 > pcount > 0):
        # raise ValueError('boundrys are 14 and 0')
        return secondarycharacter * integer
    result = pname
    for pi in range(pcount, integer):
        result += str(secondarycharacter)
    return result


async def resume_nonc(inter, edit_or_send):
    if await ismemberbanned(inter, inter.author.id):
        return

    userid = inter.author.id
    if members[userid]["lives"] < 1:
        e = None
        c = 'DEADth\nyou have been reset to q 1'

        members[userid]['int'] = 1
        members[userid]["lives"] = userbase['lives']
        members[userid]['skips'] = userbase['skips']
        if edit_or_send == 'e':
            await inter.response.edit_message(
                components=[disnake.ui.Button(
                    style=disnake.ButtonStyle.primary, label='resume', disabled=False,
                    custom_id=f'@resume.{next(qcount)}'
                ),
                ],
                embed=e,
                content=c
            )
        elif edit_or_send == 's':
            await inter.send(
                components=[disnake.ui.Button(
                    style=disnake.ButtonStyle.primary, label='resume', disabled=False,
                    custom_id=f'@resume.{next(qcount)}'
                ),
                ],
                embed=e,
                content=c
            )
        return
    try:
        uint = members[userid]['int']
    except KeyError:
        # await inter.response.edit_message(embed=disnake.Embed(description='cant find your progress'), components=[])
        if edit_or_send == 'e':
            await inter.response.edit_message(
                components=[],
                embed=disnake.Embed(description='cant find your progress'),
                content=inter.author.mention,
            )
        elif edit_or_send == 's':
            await inter.send(
                components=[],
                embed=disnake.Embed(description='cant find your progress'),
                content=inter.author.mention,
            )
        return
    emojiskkipz = f"{emojiz['skip']}"
    emojilives = f"{emojiz['bombofLives']}"
    skiprcount = members[userid]['skips']
    collec = (
            'skips::' + pnametointc((str(emojiskkipz) * skiprcount),
                                    pnameonce=str(emojiskkipz),
                                    integer=maxips,
                                    secondarycharacter=emojiz['bnone'],
                                    ) +
            f' `{skiprcount}/{maxips}`'
            '\nlives:: ' + pnametointc((str(emojilives) * members[userid]['lives']),
                                       integer=userbase['lives'],
                                       secondarycharacter=emojiz['bnone'],
                                       pnameonce=str(emojilives),
                                       ) +
            f" `{members[userid]['lives']}/{userbase['lives']}`"

    )
    if members[inter.author.id]['skips'] < 0:
        members[inter.author.id]['skips'] = 0
    if uint > qs:
        # content = ''
        embed = disnake.Embed(description='you won the quizy2')
        embed.add_field(
            name='collectables',
            value=collec,
        )
        embed.set_image(
            url='https://cdn.discordapp.com/attachments/1014972436028080238/1021435786689777674/quizyantPrize.png'
        )
        embed = gradembed(inter, embed, quiz=1)
        if edit_or_send == 'e':
            await inter.response.edit_message(
                components=[],
                embed=embed,
                content=inter.author.mention,
            )
        elif edit_or_send == 's':
            await inter.send(
                components=[],
                embed=embed,
                content=inter.author.mention,
            )
        return
    try:
        q = pool[str(uint)]
    except KeyError as err:

        comps = []
        e = disnake.Embed(description=f'KeyError: `{err}`')

        e.set_footer(text=f'you have {members[userid]["lives"]} Lives')
        if edit_or_send == 'e':
            await inter.response.edit_message(
                components=comps,
                embed=e,
            )
        elif edit_or_send == 's':
            await inter.send(
                embed=e,
            )
        return
    gas = q.get('getaskip', 0)
    collec += f'\n`{gas:+}` skips'

    disabled = q.get('disable', False)
    nint = next(qcount)
    members[userid]['qint'] = nint
    emojis = q.get(
        'emojisinstead',
        {
            '1': None,
            '2': None,
            '3': None,
            '4': None,
        }
    )
    styles: list[disnake.ButtonStyle] = [disnake.ButtonStyle.blurple, disnake.ButtonStyle.blurple,
                                         disnake.ButtonStyle.blurple, disnake.ButtonStyle.blurple]
    awnserbuttons = [
        disnake.ui.Button(
            style=styles[0],
            label=q['a'][0], disabled=disabled,
            custom_id=f'@awnser.{userid}.1.{nint}',
            emoji=emojis.get('1')
        ),
        disnake.ui.Button(
            style=styles[1],
            label=q['a'][1], disabled=disabled,
            custom_id=f'@awnser.{userid}.2.{nint}',
            emoji=emojis.get('2')
        ),
        disnake.ui.Button(
            style=styles[2],
            label=q['a'][2], disabled=disabled,
            custom_id=f'@awnser.{userid}.3.{nint}',
            emoji=emojis.get('3')
        ),
        disnake.ui.Button(
            style=styles[3],
            label=q['a'][3], disabled=disabled,
            custom_id=f'@awnser.{userid}.4.{nint}',
            emoji=emojis.get('4')
        ),
        disnake.ui.Button(
            style=disnake.ButtonStyle.link, label='stuck on the question?',
            url=SUPPORT_SERVER_INVITELINK
        ),
        disnake.ui.Button(
            style=disnake.ButtonStyle.red,
            label='skip (tezt)', disabled=False,
            custom_id=f'@skiptest.{userid}._.{nint}'
        ),
        disnake.ui.Button(
            style=disnake.ButtonStyle.red,
            label='STOP', disabled=False,
            custom_id=f'@stop.{userid}.{nint}'
        ),
    ]

    qnumb = uint + addto_question_number_quiz1
    if not q.get('dontshow_q', False):

        desc = f'({qnumb}.) ' + q['q']
    else:
        desc = f'(??.) ' + q['q']
    e = disnake.Embed(
        colour=disnake.Colour.random(),
        description=desc
    )
    # quiz 1
    if uint > 3:
        if q.get('skipDisabled', False):  # no skiping
            awnserbuttons.append(
                disnake.ui.Button(
                    style=disnake.ButtonStyle.green,
                    label='cannot skip', disabled=True,
                    custom_id=f'@Error.{nint}'
                )
            )
        else:
            awnserbuttons.append(
                disnake.ui.Button(
                    style=disnake.ButtonStyle.green,
                    label='skip', disabled=False,
                    custom_id=f'@skip.{userid}._.{nint}'
                )
            )
    else:
        awnserbuttons.append(
            disnake.ui.Button(
                style=disnake.ButtonStyle.grey,
                label='what is this?', disabled=True,
                custom_id=f'@Error.{nint}'
            )
        )
    if uint > 3:
        image = q.get('image')
        if image:
            e.set_image(url=image)

    if uint > 20 and q.get('bombEnabled', False):
        e.set_thumbnail('https://cdn.discordapp.com/attachments/1021742016515809361/1021744297973919754/bombo.png')
    ilinky = q.get('link')
    if ilinky:
        awnserbuttons.insert(
            4, disnake.ui.Button(
                style=disnake.ButtonStyle.link,
                label=q.get('linklabel', 'GOTO()'),
                url=ilinky,
            )
        )
    e.set_footer(text=f'you have {members[userid]["lives"]} Lives')
    e.add_field(
        name='collectables',
        value=collec,
    )
    if edit_or_send == 'e':
        await inter.response.edit_message(
            components=awnserbuttons,
            embed=e,
            content=inter.author.mention,
        )
    elif edit_or_send == 's':
        await inter.send(
            components=awnserbuttons,
            embed=e,
            content=inter.author.mention,
        )

c_content = """this bot was made by car7002 and has a public repository
"""
@ibot.slash_command(description='a command', name='credits')
async def credits_commands(inter):
    await inter.send(c_content, components=helpcomps)


async def resume_more(inter, edit_or_send):
    if await ismemberbanned(inter, inter.author.id):
        return
    if not SUPPORTS_A_SECOND_QUIZ:
        return
    userid = inter.author.id
    if members[userid]["lives2"] < 1:
        e = None
        c = 'DEADth\nyou have been reset to q 1'

        members[userid]['int2'] = 1
        members[userid]["lives2"] = userbase['lives2']
        members[userid]['skips2'] = userbase['skips2']
        if edit_or_send == 'e':
            await inter.response.edit_message(
                components=[disnake.ui.Button(
                    style=disnake.ButtonStyle.primary, label='resume', disabled=False,
                    custom_id=f'@2resume.{next(qcount)}'
                ),
                ],
                embed=e,
                content=c
            )
        elif edit_or_send == 's':
            await inter.send(
                components=[disnake.ui.Button(
                    style=disnake.ButtonStyle.primary, label='resume', disabled=False,
                    custom_id=f'@2resume.{next(qcount)}'
                ),
                ],
                embed=e,
                content=c
            )
        return
    try:
        uint = members[userid]['int2']
    except KeyError:
        # await inter.response.edit_message(embed=disnake.Embed(description='cant find your progress'), components=[])
        if edit_or_send == 'e':
            await inter.response.edit_message(
                components=[],
                embed=disnake.Embed(description='cant find your progress'),
                content=inter.author.mention,
            )
        elif edit_or_send == 's':
            await inter.send(
                components=[],
                embed=disnake.Embed(description='cant find your progress'),
                content=inter.author.mention,
            )
        return
    emojiskkipz = f"{emojiz['skip']}"
    emojilives = f"{emojiz['bombofLives']}"
    skiprcount = members[userid]['skips2']
    collec = (
            'skips::' + pnametointc((str(emojiskkipz) * skiprcount),
                                    pnameonce=str(emojiskkipz),
                                    integer=maxips2,
                                    secondarycharacter=emojiz['bnone'],
                                    ) +

            f' `{skiprcount}/{maxips2}`' +
            '\nlives:: ' + pnametointc((str(emojilives) * members[userid]['lives2']),
                                       integer=userbase['lives2'],
                                       secondarycharacter=emojiz['bnone'],
                                       pnameonce=str(emojilives),
                                       ) +
            f" `{members[userid]['lives2']}/{userbase['lives2']}`"

    )
    if members[inter.author.id]['skips2'] < 0:
        members[inter.author.id]['skips2'] = 0
    print(uint, qs2)
    if uint > qs2:
        # content = ''
        embed = disnake.Embed(description='you won the quizy 3\ncomback on update for more question')
        embed.add_field(
            name='collectables',
            value=collec,
        )
        embed.set_image(
            url='https://cdn.discordapp.com/attachments/1014972436028080238/1021435786689777674/quizyantPrize.png'
        )
        embed = gradembed(inter, embed, quiz=2)
        if edit_or_send == 'e':
            await inter.response.edit_message(
                components=[],
                embed=embed,
                content=inter.author.mention,
            )
        elif edit_or_send == 's':
            await inter.send(
                components=[],
                embed=embed,
                content=inter.author.mention,
            )
        return
    try:
        q = pool2[str(uint)]
    except KeyError as err:

        comps = []
        e = disnake.Embed(description=f'KeyError: `{err}`')

        e.set_footer(text=f'you have {members[userid]["lives2"]} Lives')
        if edit_or_send == 'e':
            await inter.response.edit_message(
                components=comps,
                embed=e,
            )
        elif edit_or_send == 's':
            await inter.send(
                embed=e,
            )
        return
    qnumb = uint + addto_question_number_quiz2
    gas = q.get('getaskip', 0)
    collec += f'\n`{gas:+}` skips'

    disabled = q.get('disable', False)
    nint = next(qcount)
    members[userid]['qint'] = nint
    styles: list[disnake.ButtonStyle] = [disnake.ButtonStyle.blurple, disnake.ButtonStyle.blurple,
                                         disnake.ButtonStyle.blurple, disnake.ButtonStyle.blurple]
    awnserbuttons = [
        disnake.ui.Button(
            style=styles[0],
            label=q['a'][0], disabled=disabled,
            custom_id=f'@a2wnser.{userid}.1.{nint}'
        ),
        disnake.ui.Button(
            style=styles[1],
            label=q['a'][1], disabled=disabled,
            custom_id=f'@a2wnser.{userid}.2.{nint}'
        ),
        disnake.ui.Button(
            style=styles[2],
            label=q['a'][2], disabled=disabled,
            custom_id=f'@a2wnser.{userid}.3.{nint}'
        ),
        disnake.ui.Button(
            style=styles[3],
            label=q['a'][3], disabled=disabled,
            custom_id=f'@a2wnser.{userid}.4.{nint}'
        ),
        disnake.ui.Button(
            style=disnake.ButtonStyle.link, label='stuck on the question?',
            url=SUPPORT_SERVER_INVITELINK
        ),
        disnake.ui.Button(
            style=disnake.ButtonStyle.red,
            label='skip (tezt)', disabled=False,
            custom_id=f'@skkiptest.{userid}._.{nint}'
        ),
        disnake.ui.Button(
            style=disnake.ButtonStyle.red,
            label='STOP', disabled=False,
            custom_id=f'@stop.{userid}.{nint}'
        ),
    ]
    if not q.get('dontshow_q', False):

        desc = f'({qnumb}.) ' + q['q']
    else:
        desc = f'(??.) ' + q['q']
    e = disnake.Embed(
        colour=disnake.Colour.random(),
        description=desc
    )
    if uint > 3:
        if q.get('skipDisabled', False):  # no skiping
            awnserbuttons.append(disnake.ui.Button(
                style=disnake.ButtonStyle.green,
                label='cannot skip', disabled=True,
                custom_id=f'@Error.{nint}'
            ))
        else:
            awnserbuttons.append(
                disnake.ui.Button(
                    style=disnake.ButtonStyle.green,
                    label='skip', disabled=False,
                    custom_id=f'@skkip.{userid}._.{nint}'
                )
            )
    # quiz 2
    image = q.get('image', 0)
    if image != 0 and image is not None:
        e.set_image(url=image)

    if uint > 20 and q.get('bombEnabled', False):
        e.set_thumbnail('https://cdn.discordapp.com/attachments/1021742016515809361/1021744297973919754/bombo.png')
    ilinky = q.get('link')
    if ilinky:
        awnserbuttons.insert(
            4, disnake.ui.Button(
                style=disnake.ButtonStyle.link,
                label=q.get('linklabel', 'GOTO()'),
                url=ilinky,
            )
        )
    e.set_footer(text=f'you have {members[userid]["lives2"]} Lives')
    e.add_field(
        name='collectables',
        value=collec,
    )
    if edit_or_send == 'e':
        await inter.response.edit_message(
            components=awnserbuttons,
            embed=e,
            content=inter.author.mention,
        )
    elif edit_or_send == 's':
        await inter.send(
            components=awnserbuttons,
            embed=e,
            content=inter.author.mention,
        )


@ibot.event
async def on_button_click(inter: disnake.MessageInteraction):
    customid: str = inter.component.custom_id
    userid = inter.author.id
    split: list[str] = customid.split('.')
    m = inter.message  # skiptest
    # quiz 1
    if customid.startswith('@awnser'):
        try:
            uint = members[userid]['int']
        except KeyError:
            await inter.send('this quiz is not for you')
            return
        try:
            q = pool[str(uint)]
        except KeyError as error:
            await inter.send(f'KeyError `{error}`', ephemeral=True)
            return
        if split[1] == str(userid):
            if members[inter.author.id]['qint'] is None:
                await inter.send('you do not have an active question', ephemeral=True)
                return
            scomps = m.components[0].children
            comps = []
            for b in scomps:
                if b.style == disnake.ButtonStyle.link:
                    comps.append(
                        disnake.ui.Button(
                            style=b.style, label=b.label,
                            url=b.url
                        )
                    )
                    continue
                comps.append(
                    disnake.ui.Button(
                        style=b.style, label=b.label, disabled=True,
                        custom_id=b.custom_id
                    )
                )
            # comps.pop(len(comps) - 1)
            isright = split[2] == str(q['aint'])
            if isright:
                pass
            else:
                label = 'try again'
                comps.insert(
                    4, disnake.ui.Button(
                        style=disnake.ButtonStyle.primary, label=label, disabled=False,
                        custom_id=f'@resume'
                    )
                )
            if isright:
                gas = q.get('getaskip', 0)
                if gas:
                    members[inter.author.id]['skips'] += gas
                    if members[inter.author.id]['skips'] < 0:
                        members[inter.author.id]['skips'] = 0
                if True:  # q.get('just_continue', True):
                    await gotitright(inter.author.id, True, 1)
                    await resume_nonc(inter, 'e')
            else:
                e = disnake.Embed(
                    colour=disnake.Colour.random(),
                    description='WRONG -1 life'
                )
                if q.get('bombEnabled', False) and uint > 20:
                    members[userid]["lives"] = 1
                    e.add_field(name='bombexplotion', value='the bomb has exploded')
                members[userid]["lives"] -= 1
                e.set_footer(text=f'you have {members[userid]["lives"]} Lives')

                await inter.response.edit_message(
                    components=comps,
                    embed=e
                )
        else:
            await inter.send('this question was not for you', ephemeral=True)
    elif customid.startswith('@skiptest'):
        try:
            uint = members[userid]['int']
        except KeyError:
            await inter.send('this quiz is not for you')
            return
        try:
            q = pool[str(uint)]
        except KeyError as error:
            await inter.send(f'KeyError `{error}`', ephemeral=True)
            return
        if split[1] == str(userid):
            if members[inter.author.id]['qint'] is None:
                await inter.send('you do not have an active question', ephemeral=True)
                return
            scomps = m.components[0].children
            comps = []
            for b in scomps:
                if b.style == disnake.ButtonStyle.link:
                    comps.append(
                        disnake.ui.Button(
                            style=b.style, label=b.label,
                            url=b.url
                        )
                    )
                    continue
                comps.append(
                    disnake.ui.Button(
                        style=b.style, label=b.label, disabled=True,
                        custom_id=b.custom_id
                    )
                )
            # comps.pop(len(comps) - 1)
            isright = str(userid) == '894198592670158898'
            # not q.get('skipDisabled', False) and members[inter.author.id]['skips'] > 0
            if isright:
                gas = q.get('getaskip', 0)
                if gas:
                    members[inter.author.id]['skips'] += gas
                    if members[inter.author.id]['skips'] < 0:
                        members[inter.author.id]['skips'] = 0
                await gotitright(inter.author.id, True, 1)
                await resume_nonc(inter, 'e')

            else:
                await inter.response.edit_message(
                    components=[disnake.ui.Button(
                        style=disnake.ButtonStyle.primary, label='resume', disabled=False,
                        custom_id=f'@resume.{next(qcount)}'
                    ),
                    ],
                    embed=disnake.Embed(description='Error trying to skip while its disabbled ' +
                                                    f'{repr(str(userid))}'
                                        )
                )
        else:
            await inter.send('this question was not for you', ephemeral=True)
    elif customid.startswith('@skip'):
        try:
            uint = members[userid]['int']
        except KeyError:
            await inter.send('this quiz is not for you')
            return
        try:
            q = pool[str(uint)]
        except KeyError as error:
            await inter.send(f'KeyError `{error}`', ephemeral=True)
            return
        if split[1] == str(userid):
            if members[inter.author.id]['qint'] is None:
                await inter.send('you do not have an active question', ephemeral=True)
                return
            scomps = m.components[0].children
            comps = []
            for b in scomps:
                if b.style == disnake.ButtonStyle.link:
                    comps.append(
                        disnake.ui.Button(
                            style=b.style, label=b.label,
                            url=b.url
                        )
                    )
                    continue
                comps.append(
                    disnake.ui.Button(
                        style=b.style, label=b.label, disabled=True,
                        custom_id=b.custom_id
                    )
                )
            # comps.pop(len(comps) - 1)
            isright = not q.get('skipDisabled', False) and members[inter.author.id]['skips'] > 0

            if isright:
                members[userid]["skips"] -= 1
                gas = q.get('getaskip', 0)
                if gas:
                    members[inter.author.id]['skips'] += gas
                    if members[inter.author.id]['skips'] < 0:
                        members[inter.author.id]['skips'] = 0
                await gotitright(inter.author.id, True, 1)
                await resume_nonc(inter, 'e')

            else:
                await inter.response.edit_message(
                    components=[disnake.ui.Button(
                        style=disnake.ButtonStyle.primary, label='resume', disabled=False,
                        custom_id=f'@resume.{next(qcount)}'
                    ),
                    ],
                    embed=disnake.Embed(description='Error trying to skip while its disabbled')
                )
        else:
            await inter.send('this question was not for you', ephemeral=True)
    elif customid.startswith('@resume'):
        userid = inter.author.id
        if not members.get(userid):
            members[userid] = userbase.copy()
        await resume_nonc(inter, edit_or_send='e')
    # quiz 2
    if SUPPORTS_A_SECOND_QUIZ:
        if customid.startswith('@a2wnser'):
            try:
                uint = members[userid]['int2']
            except KeyError:
                await inter.send('this quiz is not for you')
                return
            try:
                q = pool2[str(uint)]
            except KeyError as error:
                await inter.send(f'KeyError `{error}`', ephemeral=True)
                return
            if split[1] == str(userid):
                if members[inter.author.id]['qint'] is None:
                    await inter.send('you do not have an active question', ephemeral=True)
                    return
                scomps = m.components[0].children
                comps = []
                for b in scomps:
                    if b.style == disnake.ButtonStyle.link:
                        comps.append(
                            disnake.ui.Button(
                                style=b.style, label=b.label,
                                url=b.url
                            )
                        )
                        continue
                    comps.append(
                        disnake.ui.Button(
                            style=b.style, label=b.label, disabled=True,
                            custom_id=b.custom_id
                        )
                    )
                # comps.pop(len(comps) - 1)
                isright = split[2] == str(q['aint'])
                if isright:
                    pass
                else:
                    label = 'try again'
                    comps.insert(
                        4, disnake.ui.Button(
                            style=disnake.ButtonStyle.primary, label=label, disabled=False,
                            custom_id=f'@2resume'
                        )
                    )
                if isright:
                    gas = q.get('getaskip', 0)
                    if gas:
                        members[inter.author.id]['skips2'] += gas
                        if members[inter.author.id]['skips2'] < 0:
                            members[inter.author.id]['skips2'] = 0
                    if True:
                        await gotitright(inter.author.id, True, 2)
                        await resume_more(inter, 'e')
                else:
                    e = disnake.Embed(
                        colour=disnake.Colour.random(),
                        description='WRONG -1 life'
                    )
                    if q.get('bombEnabled', False):
                        members[userid]["lives2"] = 1
                        e.add_field(name='bombexplotion', value='the bomb has exploded')
                    members[userid]["lives2"] -= 1
                    e.set_footer(text=f'you have {members[userid]["lives2"]} Lives')

                    await inter.response.edit_message(
                        components=comps,
                        embed=e
                    )
            else:
                await inter.send('this question was not for you', ephemeral=True)
        elif customid.startswith('@skkiptest'):
            try:
                uint = members[userid]['int2']
            except KeyError:
                await inter.send('this quiz is not for you')
                return
            try:
                q = pool2[str(uint)]
            except KeyError as error:
                await inter.send(f'KeyError `{error}`', ephemeral=True)
                return
            if split[1] == str(userid):
                if members[inter.author.id]['qint'] is None:
                    await inter.send('you do not have an active question', ephemeral=True)
                    return
                scomps = m.components[0].children
                comps = []
                for b in scomps:
                    if b.style == disnake.ButtonStyle.link:
                        comps.append(
                            disnake.ui.Button(
                                style=b.style, label=b.label,
                                url=b.url
                            )
                        )
                        continue
                    comps.append(
                        disnake.ui.Button(
                            style=b.style, label=b.label, disabled=True,
                            custom_id=b.custom_id
                        )
                    )
                # comps.pop(len(comps) - 1)
                isright = str(userid) == '894198592670158898'
                # not q.get('skipDisabled', False) and members[inter.author.id]['skips'] > 0
                if isright:
                    gas = q.get('getaskip', 0)
                    if gas:
                        members[inter.author.id]['skips2'] += gas
                        if members[inter.author.id]['skips2'] < 0:
                            members[inter.author.id]['skips2'] = 0
                    await gotitright(inter.author.id, True, 2)
                    await resume_more(inter, 'e')

                else:
                    await inter.response.edit_message(
                        components=[disnake.ui.Button(
                            style=disnake.ButtonStyle.primary, label='resume', disabled=False,
                            custom_id=f'@2resume.{next(qcount)}'
                        ),
                        ],
                        embed=disnake.Embed(description='Error trying to skip while its disabbled ' +
                                                        f'{repr(str(userid))}'
                                            )
                    )
            else:
                await inter.send('this question was not for you', ephemeral=True)
        elif customid.startswith('@skkip'):
            try:
                uint = members[userid]['int2']
            except KeyError:
                await inter.send('this quiz is not for you')
                return
            try:
                q = pool2[str(uint)]
            except KeyError as error:
                await inter.send(f'KeyError `{error}`', ephemeral=True)
                return
            if split[1] == str(userid):
                if members[inter.author.id]['qint'] is None:
                    await inter.send('you do not have an active question', ephemeral=True)
                    return
                scomps = m.components[0].children
                comps = []
                for b in scomps:
                    if b.style == disnake.ButtonStyle.link:
                        comps.append(
                            disnake.ui.Button(
                                style=b.style, label=b.label,
                                url=b.url
                            )
                        )
                        continue
                    comps.append(
                        disnake.ui.Button(
                            style=b.style, label=b.label, disabled=True,
                            custom_id=b.custom_id
                        )
                    )
                # comps.pop(len(comps) - 1)
                isright = not q.get('skipDisabled', False) and members[inter.author.id]['skips2'] > 0

                if isright:
                    members[userid]["skips2"] -= 1
                    gas = q.get('getaskip', 0)
                    if gas:
                        members[inter.author.id]['skips2'] += gas
                        if members[inter.author.id]['skips2'] < 0:
                            members[inter.author.id]['skips2'] = 0
                    await gotitright(inter.author.id, True, 2)
                    await resume_more(inter, 'e')

                else:
                    await inter.response.edit_message(
                        components=[disnake.ui.Button(
                            style=disnake.ButtonStyle.primary, label='resume', disabled=False,
                            custom_id=f'@2resume.{next(qcount)}'
                        ),
                        ],
                        embed=disnake.Embed(description='Error trying to skip while its disabbled')
                    )
            else:
                await inter.send('this question was not for you', ephemeral=True)
        elif customid.startswith('@2resume'):
            userid = inter.author.id
        if not members.get(userid):
            members[userid] = userbase.copy()
        await resume_more(inter, edit_or_send='e')

    if customid.startswith('@stop'):
        if str(inter.author.id) == split[1]:
            await inter.response.edit_message(components=[])


@ibot.event
async def on_ready():
    # global emojiz
    getemojis()


@ibot.slash_command(
    options=[
        disnake.Option(
            type=disnake.OptionType.string,
            choices=whichquizy2,
            name='whichquizy',
            required=True
        )
    ],
    description='play this quiz',
)
async def resume(inter, whichquizy):
    await inter.response.defer()
    userid = inter.author.id
    if not members.get(userid):
        members[userid] = userbase.copy()
    # not here
    if whichquizy == 'quiz 1':
        await inter.send(
            'uhhhhhh, what,, you know?????, try my brother?',
            components=[
                disnake.ui.Button(
                    style=disnake.ButtonStyle.link, label='invite quizy ant 1',
                    url=quizyant1
                )
            ]
        )
    # pool
    elif whichquizy == 'quiz 2':
        await resume_nonc(inter, 's')
    # pool2
    elif whichquizy == 'quiz 3':
        await inter.send('this quiz is not ready yet')
        # await resume_more(inter, 's')
    # not here
    elif whichquizy == 'quiz 4':
        await inter.send(
            'uhhhhhh, what,, you know?????, unavalible??',
            components=[
                disnake.ui.Button(
                    style=disnake.ButtonStyle.link, label='invite quizy ant 1',
                    url=quizyant1
                )
            ]
        )
    else:
        await inter.send(f'testV warns about this error\nError: what is {repr(whichquizy)}')


@ibot.slash_command(description='get your rank')
async def rank(inter, user: disnake.Member = None):
    if user is None:
        user: disnake.Member = inter.author
    if user.bot:
        await inter.send('this user is a bot, he doesnt manage a rank')
        return
    try:
        members[user.id]
    except KeyError:
        await inter.send('this user has not playd any quixz yet')
        return
    exp = members[user.id]['exp']

    e = disnake.Embed(
        description=f'you have `{exp}`  points\nyou are at question {members[user.id]["int"] + 100}'
    )  # experience

    e.set_footer(text=f'you have {members[user.id]["lives"]} Lives in quiz 1 and ')
    if members[user.id]['int'] > qs:
        e = gradembed(inter, e, quiz=1)
    else:
        e.add_field(name='grade!', value='he hasnt solved all quesions')
    await inter.send(embed=e)


@ibot.slash_command(description='DELETE everything you worked for and stary=t from q1')
async def resetall(inter):
    try:
        del members[inter.author.id]  # = userbase.copy()
    except KeyError:
        await inter.send('seems like nothing is of them')
    else:
        await inter.send('success')


# @ibot.message_command(name='DELETE my message')
# async def ddm(inter, mgs: disnake.Message):
#     if mgs.author == ibot.user:
#         await mgs.delete()
#         await inter.send('success', ephemeral=True)
#     elif not mgs.author == ibot.user:
#         await inter.send('im not the author', ephemeral=True)
#     else:
#         await inter.send('wtf happend here?', ephemeral=True)


helpcomps = []
for d in linkz:
    helpcomps.append(
        disnake.ui.Button(
            style=disnake.ButtonStyle.link, label=d[0],
            url=d[1]
        )
    )


@ibot.slash_command(description='help command', name='help')
async def help_commands(inter):
    await inter.send(helpm, components=helpcomps)


class CustomError(Exception):
    pass


followups += [
    disnake.OptionChoice(
        name='announcements',
        value='1012013349204148264'
    ),
    disnake.OptionChoice(
        name='update log',
        value='1012013273647956110'
    ),
]


@ibot.slash_command(
    description='follow a channel from bot support',
    options=[
        disnake.Option(
            name='channel', description='which channel you want to recieve the announcementz',
            type=disnake.OptionType.channel,
            channel_types=[disnake.ChannelType.text],
            required=True,
        ),
        disnake.Option(
            name='fromwhich', description='which channel you want to recieve the announcementz',
            type=disnake.OptionType.string,
            choices=followups,
            required=True,
        )
    ],
    dm_permission=False,
    default_member_permissions=disnake.Permissions(manage_webhooks=True)
)
async def followit(inter, channel, fromwhich):
    # channel_from = 1012013349204148264 # announ
    # channel_from = 1012013273647956110 # update
    channel_from = int(fromwhich)
    await inter.response.defer()
    try:
        if not channel.permissions_for(inter.author).manage_webhooks:
            raise CustomError(
                'you are missing 1 of the following `VIEW_CHANNEL` `MANAGE_WEBHOOKS` and' +
                ' or some others you should give `@every1` including `SEND_MESSAGES`')

        channelfrom = await ibot.fetch_channel(channel_from)
        # noinspection PyUnresolvedReferences
        await channelfrom.follow(
            destination=channel,
            reason=f'{inter.author.name}#{inter.author.discriminator} wanted me to followit'
        )
    except disnake.Forbidden as err:
        print(err)
        await inter.followup.send(
            'im missing 1 of the following `VIEW_CHANNEL` `MANAGE_WEBHOOKS` and' +
            ' or some others you should give `@every1` including `SEND_MESSAGES`'
        )
    except CustomError as err:
        print(err)
        await inter.followup.send(err)
    else:
        await channel.send(f'<@{inter.author.id}> made me follow botsupport <#{channel_from}>\n' +
                           'to unfollow, do it your self')
        await inter.followup.send('Done')


@ibot.slash_command(
    description='awnser open ended qs',
    dm_permission=False,
    options=[
        disnake.Option(
            type=disnake.OptionType.string,
            choices=whichquizy2,
            name='whichquizy',
            required=True
        ),
        disnake.Option(
            type=disnake.OptionType.string,
            name='awnser',
            required=True
        )
    ],
)
async def dmawnser(inter, whichquizy: str, awnser: str):
    userid = inter.author.id
    m = members.get(userid)
    if m:
        # rb = None
        label = '/resume'
        if whichquizy == 'quiz 2':
            poolq = pool[str(m['int'])]
            rb = disnake.ui.Button(
                style=disnake.ButtonStyle.primary, label=label, disabled=False,
                custom_id=f'@resume'
            )
        elif whichquizy == 'quiz 3' and SUPPORTS_A_SECOND_QUIZ:

            poolq = pool2[str(m['int2'])]
            rb = disnake.ui.Button(
                style=disnake.ButtonStyle.primary, label=label, disabled=False,
                custom_id=f'@2resume'
            )
        else:
            await inter.send('invalid quiz')
            return
        dm_awnser = poolq.get('dmawnser', False)
        print(repr(awnser))
        if awnser.lower() == dm_awnser.lower():
            gas = poolq.get('getaskip', 0)
            e = disnake.Embed(
                colour=disnake.Colour.random(),
                description='congratulations you got it right'
            )
            if whichquizy == 'quiz 2':
                if gas:
                    members[inter.author.id]['skips'] += gas
                if members[inter.author.id]['skips'] < 0:
                    members[inter.author.id]['skips'] = 0
                await gotitright(inter.author.id, True, 1)
                e.set_footer(text=f'you have {members[userid]["lives"]} Lives')
            elif whichquizy == 'quiz 3':
                if gas:
                    members[inter.author.id]['skips2'] += gas
                if members[inter.author.id]['skips2'] < 0:
                    members[inter.author.id]['skips2'] = 0

                await gotitright(inter.author.id, True, 2)
                e.set_footer(text=f'you have {members[userid]["lives2"]} Lives')

            await inter.send(embed=e, components=[rb])
        else:
            e = disnake.Embed(
                colour=disnake.Colour.random(),
                description='WRONG -1 live'
            )
            if poolq.get('bombEnabled', False) and m['int'] > 20:
                if whichquizy == 'quiz 2':
                    members[userid]["lives"] = 1
                elif whichquizy == 'quiz 3':
                    members[userid]["lives2"] = 1
                e.add_field(name='bombexplotion', value='the bomb has exploded')
            if whichquizy == 'quiz 2':
                members[userid]["lives"] -= 1
                e.set_footer(text=f'you have {members[userid]["lives"]} Lives')
            elif whichquizy == 'quiz 3':
                members[userid]["lives2"] -= 1
                e.set_footer(text=f'you have {members[userid]["lives2"]} Lives')
            await inter.send(embed=e)


@ibot.slash_command(
    description='test bot only',
    dm_permission=False,
    options=[
        disnake.Option(
            type=disnake.OptionType.integer,
            name='questionz',
            required=True
        ), disnake.Option(
            type=disnake.OptionType.string,
            choices=whichquizy2,
            name='whichquizy',
            required=True
        )
    ],
)
async def setq(inter, questionz, whichquizy):
    quizyz = {
        # 'quiz 1':'int',
        'quiz 2': 'int',
        'quiz 3': 'int2',

    }
    quiz = quizyz[whichquizy]
    supposd_owner = inter.author
    userid = supposd_owner.id
    if not await ibot.is_owner(supposd_owner):
        await inter.send("this test command is only for the deleloper")
    else:
        if not members.get(userid):
            members[userid] = userbase.copy()
        q = members.get(supposd_owner.id)

        if q:
            members[supposd_owner.id][quiz] = questionz
            await inter.send("success")
        else:
            await inter.send("you are not found")


@ibot.slash_command(
    description='test bot only',
    dm_permission=False,
    options=[
        disnake.Option(
            type=disnake.OptionType.string,
            choices=whichquizy2,
            name='whichquizy',
            required=True
        ),
        disnake.Option(
            type=disnake.OptionType.integer,
            name='skips'
        ),
        disnake.Option(
            type=disnake.OptionType.integer,
            name='lives'
        ),
    ],
)
async def setskips(inter, whichquizy, skips: int = None, lives: int = None):
    quizyz = {
        'quiz 2 L': 'lives',
        'quiz 3 L': 'lives2',
        'quiz 2 S': 'skips',
        'quiz 3 S': 'skips2',

    }
    lquiz = quizyz[whichquizy + ' L']
    squiz = quizyz[whichquizy + ' S']
    supposd_owner = inter.author
    userid = supposd_owner.id
    if not await ibot.is_owner(supposd_owner):
        await inter.send("this test command is only for the deleloper")
    else:
        if not members.get(userid):
            members[userid] = userbase.copy()
        q = members.get(supposd_owner.id)
        if q:
            if skips is not None and skips <= 13:
                members[supposd_owner.id][squiz] = skips
            elif lives is not None and lives <= 7:
                members[supposd_owner.id][lquiz] = lives
            await inter.send("success")
        else:
            await inter.send("you are not found")


pass

if __name__ == '__main__':
    print(__file__)
    ibot.run(token)

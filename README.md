# why! just why!

this is quizy ant 
https://discord.com/oauth2/authorize?client_id=1014958581814141039&scope=bot+applications.commands&permissions=117760  
and this is quizy ant 2
https://discord.com/oauth2/authorize?client_id=1020976399122714675&scope=bot+applications.commands&permissions=117760

ive desided to open source the base
# what? what isit?

quizy ant is a quiz bot, it has inspiration of the impossible quiz
quizy ant's brother quizy car is the other quiz

# ask?
to ask questions with the bot
you need to follow this format if you dont want to edit the code
```json
{
  "1": {
    "q": "ask the question",
    "a": [
      "awnser 1",
      "answer 2",
      "awnser 3",
      "the fourth 4"
    ],
    "aint": 2
  }
}
```
this is the minimum for a question,  
but what does it mean?

`q` this key (tag) is the question
is the embed is it the embed description

`a` this is a list with four strings, they each represent a button

`aint` the position of the awnser in the list
ranges from 1 to four (4)

## but there are more tags (keys)
### optional tags
```json
{
    "1": {
        "q": "who is quizy ant?",
        "a": [
            "quizy ant bot 1",
            "quizy ant chapter 2",
            "you",
            "i dont know"
        ],
        "aint": 2,
        "emojisinstead": {
            "1": "<:rbx_bot:1005394280422068284>",
            "2": "<:rbx_bot270:1006192955889029161>",
            "3": "<:rbx_bot90:1006192946720288849>",
            "4": "<:rbx_bot180:1006192951237550140>"
        },
        "dmawnser": "",
        "disable": true,
        "dontshow_q": true,
        "just_continue": true,
        "image": "",
        "getaskip": 1,
        "bombEnabled": true,
        "skipDisabled": true,
        "link": "https://github.com/Qin2007/quizyantBase/settings",
        "linklabel": "car7002's github"
    }
}
```

`emojisinstead` this tag is to use buttons with emojis  
`link` if you want to redirect users to a site, do it here  
`linklabel` the label that shows on the button  
`dmawnser` if a value is set,
the user can also move on if he provides the eggact value in the command with the same name  

`disable` if true the buttons are disabled (only set to true if dmawnser is also provided)  
`getaskip` if it is a nonZER0 value this adds to the skip counter (if negative it removes intead)  
`dontshow_q` if true it shows ?s instead of numbers  
`image` the image to attach to the embed, if empty no images will be there  
`just_continue` practicly useless (left over of the test version) 
if it was false, the bot would congratulate for getting it right
no one does that noAdays  
`bombEnabled` if true if the player makes even 1 missTake he loses all lives except 1
then 1 for getting it wrong resulting in a game over  
`skipDisabled` if true the player cannot skip the question
in any way  

## userbase

you have a userbase dict in the code
search it up
it works like this
```python
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
```

`int` this key is the question the player is on  
`exp` this key is the expiriance the player has, it is not very evective  
`qint` even i dont know what it is (but dont change it, ok?)  
`lives` the starter lives of the player in the first quiz  
`skips` the starter skips of the player in the first quiz  

`lives2` works the same as `lives` except its for the second quiz  
`skips2` works the same as `skips` except its for the second quiz  
`int2` works the same as `int` except its for the second quiz  

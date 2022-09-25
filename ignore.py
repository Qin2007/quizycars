import botBase
#
bot = botBase # this block below is to calculate the skips in the first quiz
# getaskkip = bot.userbase['skips']
# print('starter skips',getaskkip)
# for i, v in bot.pool.items():
#     ii = v.get('getaskip', 0)
#     getaskkip += ii
#     if ii:
#         print(i, f'{ii:+} for a total of', getaskkip)
# print('p=', getaskkip)
# print('total=', getaskkip)
# print('lives + skips =', getaskkip + bot.userbase['lives'],'\n')
pass # this block below is to calculate the skips in the second quiz
# getaskkip = bot.userbase['skips2']
# print('2\'s starter skips',getaskkip)
# for i, v in bot.pool2.items():
#     ii = v.get('getaskip', 0)
#     getaskkip += ii
#     if ii:
#         print(i, f'{ii:+} for a total of', getaskkip)
# print('p2=', getaskkip)
# print('lives2 + skips2 =', getaskkip + bot.userbase['lives2'])
pass
# for i, v in bot.pool.items():
#     ii = v.get('bombEnabled')
#     if ii is True:
#         print(i, ii)
pass
# for i, v in bot.pool.items():
#     ii = v.get('skipDisabled')
#     if ii is True:
#         print(i, ii)
pass
# for i, v in bot.pool2.items():
#     ii = v.get('bombEnabled')
#     if ii is True:
#         print(i, ii)
pass
# for i, v in bot.pool2.items():
#     ii = v.get('skipDisabled')
#     if ii is True:
#         print(i, ii)
pass # these are for all questions
print('len all', len(bot.pool))
if bot.SUPPORTS_A_SECOND_QUIZ:
    print('len all', len(bot.pool2), 'quiz 2')

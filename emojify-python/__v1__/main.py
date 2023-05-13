
# todo(@joeysapp @ 2023-04-23): made this a lot better imo
# - Figure out emoji generation and things like: 🖑emojis!!!! also
# 🗙🗙🗙🗘🗗🗖🗕🗕🗖🗕🗓🗑🗐🖡🖟🖝🖜🖙🖚🖙🖗🖙🖙🖖🖘🖖🖙🖛🖜🖘🖖🖘🖚🖘🖕
#   - (Above are just plain ascii hands, I think
# - Figure out emoji classifications, like word<->emojis or even sentence<->emojis :^)
# - Lol, just generally how best to do %s with if/eleses? e.g. adding a stutter-er possibility or something
# - ----> Dictionary/sysnonyms/antonyms lolololo

# note(@joeysapp): Discord messages are limited to 2,600 chars, and the emojis get turned into :water_buffalo:, so

def randomInt():
  return math.floor

def randomPick(_list):
  return _list[math.floor(random.random()*len(_list))]

def getAsciiFace():
  faces = [
    '(๑˃ᴗ˂)ﻭ', 
    '(˘ω˘)', 
    '(*＾3＾)',
    '(✿◠‿◠)',
    'ฅ(＾・ω・＾ฅ)'
    '(｡･ω･｡)ﾉ♡',
    '(≧◡≦)ﾉ',
    '(⁄ ⁄•⁄ω⁄•⁄ ⁄)',
    '(๑ↀᆺↀ๑)',
    '(｡♥‿♥｡)',
    '(・ω´・)', 
    '(｡･ω･｡)', 
    '(´ ▽ ` )ﾉ',
    '(๑˃̵ᴗ˂̵)', 
    # 'UwU', 'uwu', 'uwU', 'Uwu', 'OwO', 'OWO', 'owo', 'Owo', 'owO',
  ]
  return randomPick(faces)


def stutter(word):
  return word

def uwu():
  return 'uwu'

def lispify(text_list=[]):
  # text = text.replace('r', 'uwu')
  ret = []
  for text in text_list:
    t = text.replace('r', 'w')
    t = text.replace('l', 'w')
    ret.append(t);
    print('ret', t, text, ret)
  return ret

def uwuify(text_list=[]):  
  ret=[]
  for text in text_list:
    t = text.replace('u', 'uwu')
    t = text.replace('oo', 'uwu')
    t = text.replace('o', 'owo')
    ret.append(t)
  return ret

# Returns a list of ussified nouns
def ussify(noun):
  ussys = []
  vowels = 'aeiou'
  for idx in range(len(noun)-1):
    if not noun[idx].lower() in vowels:
      ussys.append(noun[:(idx+1)]+'ussy')
  return ussys


def getSexualPhrase():
  ejaculatives = [
    'baka' 
    'o' * math.floor(1+random.random()*5) + 'h',
    'n' * math.floor(2+random.random()*5) + 'g',
  ]
  adjectives = ['senpai', 'sexy', 'uwu', 'desu']
  return randomPick(ejaculatives) + ' ' + randomPick(adjectives)

  

def doMarkdownEmphasis(word):
  # italic, underline, bold, strike, spoiler?
  return word

# How to make this @ someone on a paste?
def isDiscordUser(word):
  return '@'+word

def canModifyEmoji(emoji):
  return False

# lol, this is messy.
skin_tones = [127995, 127996, 127997, 127998, 127999]
mac_exceptions = [
  127892, 127893, 127896, 127900, 127901, 127985, 127986,
  [i for i in range(128318, 128328)], 128335, [i for i in range(128360, 128366)], [i for i in range(128379, 128390)],
  128392, 128393, 128398, 128399, [i for i in range(128401, 128404)], [i for i in range(128407, 128419)],
  128422, 128423, [i for i in range(128425, 128432)], [i for i in range(128435, 128443)], [i for i in range(128445, 128449)],
  [i for i in range(128453, 128464)], [i for i in range(128468, 128475)], 128479, 128480, 128482, [i for i in range(128484, 128487)],
  [i for i in range(128489, 128494)], [i for i in range(128496, 128498)], [i for i in range(128500, 128505)],
  # Additional
  127778, 127779, 127892, 127893, 127896, 127900, 127901, 127985, 127986, 127990,
  # Additional Skin tones
  127995, 127996, 127997, 127998, 127999,
  128254,
]
for sublist in mac_exceptions:
  if isinstance(sublist, list):
    for item in sublist:
      mac_exceptions.append(item)

import random
import subprocess
import math

from alphabet import bible
all_emojis = []
options = None

DEBUG = True
DO_DISCORD_EMOJIS = True
def getDefaultOptions():
  return {
    # Probabilities for what a word can turn into.
    # < 1 means you will see plain text.
    'unicode': 0.01,
    'emoji': 0.2,
    
    'emoji_repeat': 0.76, # Ideal = 0.78
    'emoji_move_velocity': 1.25, # ideal = 1.5
    'emoji_reset': 0.05, # ideal = 0.1
    
    'unicode_idx': math.floor(random.random()*len(bible['a'])),
    'unicode_reset': 0.15 # Probability on a loop that we pick a new unicode type
  }
options = getDefaultOptions()

def map(val, min1, max1, min2, max2):
  return min2+(max2-min2)*((val-min1)/(max1-min1))

# http://www.unicode-symbol.com/u/00A0.html
def getSpace():
  return '\u00A0'

def write_to_clipboard(output):
  process = subprocess.Popen(
    'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
  process.communicate(output.encode('utf-8'))

# Emoticons
for idx in range(128512, 128591):
  res = u'\\U%08x' % idx
  if DEBUG:
    print('Emoticons['+str(idx)+']: '+res.encode().decode('unicode_escape'), end='')
  if idx not in mac_exceptions:
    all_emojis.append(res)
    print()
  else:
    print('== macOS Exception, do not add')

# Symbols, e.g. ✸ ❎ ➣
# for i in range(9986, 10160):
#   res = u'\\u%x' % i
#   if DEBUG: print('Symbols['+str(i)+']: '+res.encode().decode('unicode_escape'))
#   all_emojis.append(res)

# # Transport/Map Symbols
for idx in range(128640, 128704):
  res = u'\\U%08x' % idx
  # transport.append(res)
  if DEBUG:
    print('Transport['+str(idx)+']: '+res.encode().decode('unicode_escape'), end='')
  if idx not in mac_exceptions:
    all_emojis.append(res)
    print()
  else:
    print('== macOS Exception, do not add')

# Enclosed Symbols
# for i in range(127344, 127569):
#	res = u'\\U%08x' % i
#	enclosed_symbols.append(res)

# Misc
for idx in range(127745, 128511): 
  res = u'\\U%08x' % idx
  # misc.append(res)
  if DEBUG:
    print('Misc['+str(idx)+']: '+res.encode().decode('unicode_escape'), end='')
  if idx not in mac_exceptions:
    all_emojis.append(res)
    print()
  else:
    print('== macOS Exception, do not add')

print(mac_exceptions)

# Additional Emojis
# for i in range(127745,128511): # Includes stuff like clocks, mosques.. but lots of non-mac stuff.
for idx in range(127745, 128317):
  res = u'\\U%08x' % idx
  # misc.append(res)
  if DEBUG:
    print('Additional['+str(idx)+']: '+res.encode().decode('unicode_escape'), end='')
  if idx not in mac_exceptions:
    all_emojis.append(res)
    print()
  else:
    print('== macOS Exception, do not add')

def getRandomUnicodeText(word, unicode_idx=None, unicode_reset=0):
  if DEBUG: print('* getRandomUnicodeText('+str(word)+')')
  alpha = 'abcdefghijklmnopqrstuv'
  translations = [[] for e in range(len(bible['a']))]
  for idx in range(len(bible['a'])):
    new_word = ''
    for letter in word:
      new_char = ''
      if letter in bible:      
        new_char = bible[letter][idx]
        # if DEBUG: print('* getRandomUnicodeText(letter=', letter, ') ->', bible[letter][idx])
      if letter == '' or letter not in bible:
        new_char = letter
        # if DEBUG: print('* getRandomUnicodeText(letter=', letter, ') !!!! -> No translation ->', letter)
      new_word += new_char
    translations[idx] = new_word
    # if DEBUG: print('* getRandomUnicodeText('+str(word)+') ->', new_word)
  if (random.random() < unicode_reset):
    unicode_idx = math.floor(random.random() * len(bible['a']))
  return translations[unicode_idx]

def getEmojisByText(source, idx, prob, reset_prob):
  if DEBUG:
    print('getEmojisByText(source=[...] idx=', idx, ' prob=', prob, ', reset_prob=', reset_prob, ') len(all_emojis)=', len(all_emojis))
  result = ''
  char = source[idx]
  current_emoji_idx = math.floor(random.random() * len(all_emojis))
  if char in all_emojis:
    # If the item we're looking at is an emoji, just add the emoji. Or duplicate it?
    current_emoji_idx = all_emojis.index(char)
  current_emoji_idx = current_emoji_idx % len(all_emojis)
  chunk = []
  keep_adding_emojis = True
  while (keep_adding_emojis):
    chunk.append(all_emojis[current_emoji_idx].encode().decode('unicode_escape'))
    possible_distance = options['emoji_move_velocity'] or random.random()*50;
    div = 1
    if (isinstance(possible_distance, float)):
      div = 100;
    move_idx_by = math.floor(random.randrange(-possible_distance*div, possible_distance*div)/div)
    current_emoji_idx += move_idx_by
    current_emoji_idx = current_emoji_idx % len(all_emojis)
    if (random.random() < reset_prob):
      current_emoji_idx = math.floor(random.random() * len(all_emojis))
    if (random.random() > prob):
      keep_adding_emojis = False  
  # Where does the actual word go?
  insert_idx = math.floor(random.random() * len(chunk))
  # Should we pad the original word with spaces?
  pad_start = ' '*math.floor(random.random()*2)
  pad_end = ' '*math.floor(random.random()*2)
  chunk.insert(insert_idx, pad_start+source[idx]+pad_end)
  result += (''.join(e for e in chunk))
  if DEBUG: print('getEmojisByText() -> ', result)
  return result

#     _	   ____	 ____  
#    / \  |  _ \|  _ \ 
#   / _ \ | |_) | |_) |
#  / ___ \|  __/|  __/ 
# /_/ 	\_\_|	 |_|    
		     
loop = True
input_text = ''
# if DEBUG: input_text = 'You know, this is really messing with my recently-used emojis'.split()
orig_text = input_text
fin_text = ''
print('<INFO> Silly probabilistic emojifier')
print('<INFO> A number of ascii/emojis won\'t show up in zsh.')
print('<OPTS> ', options)
while loop:
  print('<========== [ MAIN ] ==========>')
  fin_text = ''
  if (input_text == ''):
    print(' Please input a string.')
    input_text = input(' > ')
    orig_text = input_text
    input_text = input_text.split()
  for i in range(len(input_text)):
    new_text = ''    
    if not input_text[i][0].isalnum() or input_text[i][0].isupper() or len(input_text[i]) < 3:
      if input_text[i][0] == '@' or (len(input_text[i]) > 1 and input_text[i][1] == '@'):
        # fin_text += randomPick(ussify(input_text[i][1:])) + ' (' + input_text[i] + ') '
        fin_text += '@' + randomPick(ussify(input_text[i][1:])) + ' '
      else:
        fin_text += input_text[i] + ' '
      continue
    emoji_result = getEmojisByText(input_text, i, options['emoji_repeat'], options['emoji_reset'])
    unicode_result = getRandomUnicodeText(input_text[i], options['unicode_idx'], options['unicode_reset'])
    plain_result = input_text[i]
    dice_roll = random.uniform(0, 1)
    if DEBUG: print('(MAIN.000) input_text=', input_text)
    if DEBUG: print('(MAIN.000) options=', options)
    if DEBUG: print('(MAIN.000) dice_roll=', dice_roll)
    # [0.3, 0.1] and roll a .4
    # Emojis 30% of the time, unicode 10% of the time, nothing 60% of the time.
    #
    # [0.1, 0.9] and roll a .5
    # Emojis 10% of the time, unicode 90% of the time.
    probs = [
      { 'n': 'emoji', 'p': options['emoji']},
      { 'n': 'unicode', 'p': options['unicode']},
      { 'n': 'plain', 'p': abs(1 - options['emoji'] - options['unicode'])},
    ]
    probs.sort(key=lambda p: p['p'])
    # note(2023-04-22): lol at this. rip me and my brain. can't handle equal probabilities..
    if DEBUG: print("(MAIN.001) probabilities=", probs)
    if (dice_roll < probs[0]['p']):
      if probs[0]['n'] == 'emoji': new_text = emoji_result
      if probs[0]['n'] == 'unicode': new_text = unicode_result
      if probs[0]['n'] == 'plain': new_text = plain_result
    elif (dice_roll <= probs[1]['p']):
      if probs[1]['n'] == 'emoji': new_text = emoji_result
      if probs[1]['n'] == 'unicode': new_text = unicode_result
      if probs[1]['n'] == 'plain': new_text = plain_result
    else:
      if probs[2]['n'] == 'emoji': new_text = emoji_result
      if probs[2]['n'] == 'unicode': new_text = unicode_result
      if probs[2]['n'] == 'plain': new_text = plain_result
    if DEBUG: print("(MAIN.002) new_text=", new_text)
    ## Actually adding the text
    space = ' '
    if bible['a'][options['unicode_idx']] == 'ａ':
      # Handling 
      space = ' '*5
    if (random.random() < 0.1):
      new_text += getAsciiFace() + ' '
    fin_text += new_text + space
    if DEBUG: print('=====================\n')
  print('<ORIG>')
  print('\t', orig_text)
  print('<OPT>')
  print('\t', options)
  print('<SRC>')
  # if DEBUG: print('\t', input_text)
  print('\t', ' '.join(e for e in input_text))
  print('<RES>')
  print('\t', fin_text)
  print()
  # random.shuffle(fin_text)
  # write_to_clipboard(' '.join(e for e in fin_text))
  write_to_clipboard(fin_text)
  print('<========== [ MENU ] ==========>')
  menu_choice = input(' [ R ] Repeat from <SRC> string\n [ C ] Repeat with <RES> string\n [ O ] Update settings\n\n [ U ] Uwu-ify string\n [ X ] Reset to original string\n [ N ] Input a new string\n [ Q ] Copy to clipboard and quit\n\n > ')
  menu_choice = menu_choice.lower()
  if menu_choice == 'r' or menu_choice == '':
    continue
  elif menu_choice == 'x':
    if isinstance(orig_text, list):
      input_text = orig_text
    else:
      input_text = orig_text.split()
  elif menu_choice == 'c':
    input_text = fin_text.split()
  elif menu_choice == 'o':
    print("\t\t<TODO ADD OTHER OPTION CONFIGS HERE>")
    probabilities_updated = False
    while not probabilities_updated:
      new_emoji_prob = float(input('<PROB.emoji='+str(options['emoji'])+'> updated to: '))
      new_unicode_prob = float(input('<PROB.unicode='+str(options['unicode'])+'> updated to: '))
      if (new_emoji_prob + new_unicode_prob <= 1):
        options['emoji'] = new_emoji_prob
        options['unicode'] = new_unicode_prob
        probabilities_updated = True
      else:g
        print('<ERROR> Your two probabilities must sum to 1.')
  elif menu_choice == 'c':
    input_text = fin_text
  elif menu_choice == 'u':
    input_text = fin_text.split()
    input_text = lispify(input_text)
    input_text = uwuify(input_text)
    # write_to_clipboard(fin_text)
  elif menu_choice == 'q':
    write_to_clipboard(' '.join(e for e in input_text))
    loop = False
  else:
    orig_text = menu_choice
    input_text = menu_choice.split()



# Oh my goodness me oh my it's Emanick's actual birthday?? It just so happens is brother's in-laws Eid al-Fitr party is today too?? Happy birthday unless he's being very clever with Sal's events, knowing we all check so regularly!!
#




# 2019-1-17 Addition to Qaz.wtf
# 2023-04-22: Currently not used
# import requests
# import html
# QAZRequests = {}
# def getRandomQAZText(word):
#   if word in QAZRequests:
#     return random.choice(QAZRequests[word])	
#   words = []
#   res = requests.get("http://qaz.wtf/u/convert.cgi?text="+word).text
#   res = res[res.find('table'):]
#   while (len(res) > 10) and len(words) < 35:
#     res = res[res.find('</td><td>')+9:]
#     word = (res[res.find('\n')+1:res.find('\n</td>')])
#     word = html.unescape(word)
#     words.append(word)
#     words.pop(17)
#     QAZRequests[word] = words    
#   return random.choice(words)


# def getRandomEmojis():
#   res = ""
#   emoji_pick = math.floor(random.random()*len(all_emojis))
#   c = random.random()
#   while (c > 0.6):
#     c = c - random.uniform(0,1)
#     res = res + all_emojis[emoji_pick].encode().decode('unicode_escape')
#     emoji_pick += 1
#   return res

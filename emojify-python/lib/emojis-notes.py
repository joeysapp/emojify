

# old. Potentially useful for javascript/ other implementations?
woman = Emoji('👩',  b'\\U0001f469')

def isEmojiModifiable(emoji):
    unicode = [b'\\u0001f44b']
    emojis = ['__hand__', '💑', '👩']
    return 

def getEmojiCombinations(emoji):
    combinations = []
    return combinations

# Note: do not return the yellow version, because not usable in annotations (?)
def getEmojiColors(emoji):    
    # color_unicodes = [b'\\U0001f3fb', b'\\U0001f3fc', b'\\U0001f3fd', b'\\U0001f3fe', b'\\U0001f3ff']
    color_emoji = ['🏻', '🏼', '🏽', '🏾', '🏿']
    color_strings = []
    for c in color_emoji:
        new_color = "{}{}".format(emoji, c);
        color_strings.append(new_color)
    return color_strings

class Character():
    def __init__(self, *args, **kwargs):
        self.decimal = kwargs.get('decimal') or args[0] or 0
        # I think hex is largely not needed, unless a lot of documentation is hex based?
        self.binary = kwargs.get('binary') or bin(self.decimal)
        self.hex = kwargs.get('hex') or hex(self.decimal)
        self.id = "Character\n* {}\n* {}\n* {}".format(self.decimal, self.hex, self.binary)
        # Below are actual emoji/unicode usefulness
        self.unicode_string = decimalToUnicode(self.decimal)
        self.unicode_encode = encodeUnicode(self.unicode_string)
        self.unicode_decode = decodeUnicode(self.unicode_encode)
    def __repr__(self):
        return "{}{}".format(self.id, self.unicode_info())
    def unicode_info(self):
        return "\n* unicode_string='{}'\n  -> unicode_encode='{}'\n  -> unicode_decode='{}'".format(self.unicode_string, self.unicode_encode, self.unicode_decode)

def decimalToUnicode(decimal):
    return u"\\U%08x" % decimal

def encodeUnicode(unicode_string):
    return unicode_string.encode()

def decodeUnicode(unicode_encoded):
    return unicode_encoded.decode('unicode_escape')











>>> print('👩🏼‍❤️‍💋‍👨🏿'.encode())
b'\xf0\x9f\x91\xa9\xf0\x9f\x8f\xbc\xe2\x80\x8d\xe2\x9d\xa4\xef\xb8\x8f\xe2\x80\x8d\xf0\x9f\x92\x8b\xe2\x80\x8d\xf0\x9f\x91\xa8\xf0\x9f\x8f\xbf'
>>> print('👩🏼‍❤️‍💋‍👨🏿'.encode('unicode_escape'))
b'\\U0001f469\\U0001f3fc\\u200d\\u2764\\ufe0f\\u200d\\U0001f48b\\u200d\\U0001f468\\U0001f3ff'

"🏾" ->
"🏾".encode() ->
b'\xf0\x9f\x8f\xbe' which is .. BINARY, four hex items. I think? uhhh. 000^1
b'\xf0\x9f\x8f\xbe'.decode() -> "🏾"
"😀"
* b'\xf0\x9f\x98\x80'
* b'\\U0001f600'
* 128512

"🏾"
* b'\xf0\x9f\x8f\xbe'
* b'\\U0001f3fe'
* 127998

"🏾".encode('unicode_escape') ->
* b'\\U0001f3fe' which is 127998 in decimal
* b'\\U0001f3fe'.decode() -> "b'\\U0001f3fe'"
* b'\\U0001f3fe'.decode() -> "🏾"

# Unicode(dec=8 hex_string='\U00000008', encoded_hex=b'\\U00000008', decoded_hex)
# Unicode(dec=128511 hex_string='\U0001f5ff', encoded_hex=b'\\U0001f5ff', decoded_hex=🗿)
# EMOJI MODIFIER FITZPATRICK TYPE-5
# 🙎  🏾🙎 🏾🙎🏾🙍‍♂️🙎🏾".sp
# 🙎
# 💑 🧑🏼‍❤️‍💋‍🧑🏾
# 💑 🧑🏼‍❤️‍💋‍🧑
# 🧑🏼‍❤️‍💋‍🧑🏼
# 🧑🏼‍❤️‍💋‍🧑🏼 -> pasting this in other apps will fix it..
# 👩‍❤️‍💋‍👩👩‍❤️‍💋‍👩👩‍❤️‍💋‍👩 👩‍❤️‍💋‍👩 
👩🏼‍❤️‍💋‍👨🏿
👩🏼‍❤️‍💋‍👨🏿
# 👩🏼‍❤️‍💋‍👨
# len('👩') = 1
# len('👩🏻') = 2
# len('👩‍❤️‍👩') = 6 = 👩‍❤️👩‍

👩
❤️
👩
# len('👩‍❤️‍💋‍👩') = 8

ZERO_WIDTH_CHARACTER = '‍'
zwc = ZERO_WIDTH_CHARACTER
zwc_u = b'\\u200d'
woman = { 'emoji': '👩', 'unicode': b'\\U0001f469' }
heart = '❤️'
foo = '{}{}{}{}{}'.format(woman, ZWC, heart, ZWC, woman)

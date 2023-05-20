IDEA:

Should types + generators + mutators be held in the Node type?
Or should all the mutators/generators be in the "Probabilities" thing?

# NodeTypes
# Sentence - which contains a list of other NodeTypes
#      Word
#        - User
#        - Noun, verb, etc
#      Symbol
#        - Punctuation ,. !?;:
#        - Emoji
#        - Misc %#
class NodeType():
    def __init__(self, value=None, *args=[], **kwargs):
        self.value = value
        self.type = self.getType(value)
        self.sentiment = None # getSentiment(value)

    def mutate(self, function):
        return None    

    def getType(self, val):
        return None


class Sentence():
    def __init__(self, *args, **kwargs):
        self.source = ''
        self.words = []
        self.history = []

class Word():
    def __init__(self, *args, **kwargs):
        self.source = ''
        self.history = []
        # TODOS
        self.sentiment = []
        # Actions (or functions/mutators/decorators) that have been done to it?
        self.actions = []

    def __repr__(self):
        return "Word({})".format(self.__dict__)


# IDEAS
# noun, verb, preposition, adjective, adverb
# punctuation, period/comma/exclamation/questionmark

# user
# emoji, emoticon
class WordType():
    def __init__(self, *args, **kwargs):
        self.type = ''

    def __repr__(self):
        return "WordType({})".format(self.__dict__)











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

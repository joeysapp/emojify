import random
import subprocess
import math

from .src import alphanum, emojis, get_space
lib = [emojis]

def map(val, min1, max1, min2, max2):
  return min2+(max2-min2)*((val-min1)/(max1-min1))

def write_to_clipboard(output):
  process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
  process.communicate(output.encode('utf-8'))

def get_random_emojis(word) -> list:
  idx = math.floor(random.random()*len(emojis))
  to_add = emojis[idx].encode().decode('unicode_escape')
  return [to_add]

while (True):
  input_text = "hello this is a test of a reasonably-lengthed sentence. with periods?"
  input_text = input_text.split();
  fin_text = []
  for i in range(len(input_text)):
    new_text = []
    new_text.extend(get_random_emojis(input_text[i]))
    new_text.extend([input_text[i]])
    fin_text.extend(new_text)
  fin_string = ' '.join(w for w in fin_text)
  print("{}".format(fin_string))
  write_to_clipboard(fin_string)
  exit()
      




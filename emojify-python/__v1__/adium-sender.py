import keyboard
from os import system
from platform import system as platform
import random, math
import subprocess

emoji_ranges = [[0x1F100,0x1F64F],[0x1F680,0x1F6FF],[0x1F910,0x1F96B],[0x1F980,0x1F9E0]]

# for i in range(0x1F100,0x1F64F):
# 	print((u'\\U%08x' % i).decode('unicode-escape'))


def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

def getEmoji():
	res = " "
	amt = int(random.uniform(0, 3))
	for i in range(0, amt):
		t_range = random.choice(emoji_ranges)
		t_emoji = random.randrange(t_range[0], t_range[1])
		res = res + ((u'\\U%08x' % t_emoji).decode('unicode-escape'))
	return res

while (True):
	txt = raw_input('> ').split()
	res = ""
	for i in range(len(txt)):
		if random.random() > 0.5:
			res = res + txt[i] + getEmoji()+" "
		else:
			split_idx = int(math.floor(random.random()*len(txt[i])))

			res = res + txt[i][0:split_idx]+getEmoji() + txt[i][split_idx:] + " "
	cmdSend = """osascript -e 'tell application "Adium" to send the active chat message "%s"'""" % res
	subprocess.Popen(cmdSend, shell=True).wait()
	# system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Steam" to true' ''')
	# write_to_clipboard(res)
	# keyboard.press_and_release('command+v, enter')
	# system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Terminal" to true' ''')

	# print(res)

# if platform() == 'Darwin':  # How Mac OS X is identified by Python
	# system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Steam" to true' ''')

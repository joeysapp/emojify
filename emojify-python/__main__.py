#!/usr/bin/python3.8
"""
Interactive tool for messing with text
$ cd ../
$ python3.8 -m emojify-python
"""
# -- V2 Goals
# Agnostic enough to be used in Javascript on website/discord
# Main loop is easier to use (step forward/step backward, etc.)
## I want a function that I can pass an arbitrary number of functions to, with probabilities for each.
## I want the function to roll a seeded random number and then execute a function if it matches the probability
## 
## Maybe I'd like, put each function into a list N times for each function and then randomly pick one? That seems kind of silly
# What is "Main Loop"?


import sys, textwrap, time, math

# from text_mutators import stutter, asciiText
# from text_adders import emojis, asciiFaces, asciiDecorators
# from text_finishers import uwuify, mentions,
from .types import Word, WordType
# from methods import 

example1 = 'haha you so silly zazzy how could you say that XD'
example2 = 'I just want out of this prison!!!'

def main() -> int:
    print('Please input a string.')
    input_text = input(' > ')    
    while True:
        # [ Do something to text ]
        words = input_text.split()
        #  * Loop through entire string, look at each word/space/emoji/ascii and getFunction for it
        #    - Pros: 
        #  * Pick a random word/space/emoji/ascii and getFunction for it
        #    - Pros: More granular string creation, more involved. or, loopable.
        # [ Ask for next step ]
        next_steps = {
            'r': '[ R ] Repeat with previous string',
            'c': '[ C ] Repeat with current string',
            'x': '[ X ] Reset to original string',
            'n': '[ N ] Input a new string',
        }
        for step_key in next_steps.keys():
            print(next_steps[step_key])
        input_step = ''
        while input_step not in next_steps:
            input_step = input(' > ')
        














# note(@joeysapp): this is so C-c won't kill python first before closing the plotter serial connection
import signal
from threading import Event
exit_signal = Event()
def handle_interrupt(signal, _frame):
    Console.error("\n", signal, _frame, "\n");
    std_result = 1
    exit_signal.set()
for s in ('TERM', 'HUP', 'INT'):
    signal.signal(getattr(signal, 'SIG'+s), handle_interrupt);

sys.exit(main())

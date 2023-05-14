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
from .types import Sentence, Word, WordType
from .functions import modify
# from methods import 

example1 = 'haha you so silly zazzy how could you say that XD'
example2 = 'I just want out of this prison!!!'

# todo(joeysapp): Make this an actual linked list
class Step():
    def __init__(self, *args, **kwargs):
        self.clear()

    def __repr__(self):
        return "original={}\nprevious={}\ncurrent={}\nnext={}".format(self.original, self.previous, self.current, self.next)

    def generate(self):
        # Change string, 'uwu's, 'stuttering', 'ascii change', 'LANGAUGE????', 'ModifyMeaningOfWord'
        new_string = modify(self.current)
        # Add items into string, emojis, emoticons, exclamations, phrases
        new_string = generate(self.current)
        self.next = new_string;

    # While this isn't a truly linked list, we can't have more than one 'back' step
    def back(self):
        tmp = self.current
        self.current = self.previous;
        self.previous = self.current

    def forward(self):
        self.previous = self.current
        self.current = self.next
    
    def reset(self):
        self.previous = self.current
        self.current = self.original        

    def clear(self):
        self.original = None
        self.current = None
        self.previous = None

def main(step = Step()) -> int:
    # [ Get the string to do something to ]
    if not step.current:
        step.current = input('Please enter a string\n> ')
        step.original = step.current
        
    # [ Modify text ]
    step.generate()
    print(step)
    
    # [ Ask for step ]
    choice = ''
    steps = {
        'f': { 'function': step.forward, 'msg': '[ F ] Step forwards' },
        'b': { 'function': step.back, 'msg': '[ B ] Step backwards' },
        'r': { 'function': step.reset, 'msg': '[ R ] Reset' },
        'n': { 'function': step.clear, 'msg': '[ N ] New string' },
        'q': { 'function': exit, 'msg': '[ Q ] Quit' },
    }
    for step_key in steps.keys():
        print(steps[step_key]['msg'])
    while choice not in steps:
        choice = input(' > ').lower()

    fn = steps[choice]['function']
    fn()
    main(step)



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

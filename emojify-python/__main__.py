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



#         color = "green" if command else "gray-0"
#         cmd_str = "\"" + str(command) + "\"" if command else "None"
#         Console.puts("\n\t-> {}, {}\n".format(
#             Console.format(cmd_str, [color, "bold" if command else "italic"]),
#             Console.format(pos, [color, "italic"])))



import sys, textwrap, time, math

from .lib import Graph

example1 = 'haha you so silly zazzy how could you say that XD'
example2 = 'I just want out of this prison!!!'

def main(graph = None) -> int:
    # [ Get the string to do something to ]
    if not graph:
        graph = Graph(input('Please enter a string\n> '))
        
    # [ Modify text ]
    graph.generate_next(amount=3)

    # [ Do it over again ]
    main(graph)




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

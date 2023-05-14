#!/usr/bin/python3.8
"""
Interactive tool for messing with text
$ cd ../
$ python3.8 -m emojify-python
"""
# -- V2 Goals
# Agnostic enough to be used in Javascript on website/discord
# Main loop is easier to use (step forward/step backward, etc.)

import sys, textwrap, time, math
from .lib import Graph, Probabilities

example1 = 'haha you so silly zazzy how could you say that XD'
example2 = 'I just want out of this prison!!!'

def main(graph = None) -> int:
    # [ Get text ]
    if not graph:
        graph = Graph(example1)
        # graph = Graph(input('Please enter a string\n> '))
    
    # [ Modify/add text ]
    probabilities = Probabilities([
        # Generators
        # Are "probabilities"/occurence chances per word, or..
        # Like, "generators" probably should .. generate a string, and then 
        #    place that string at a random place in the string. right?
        { fn: genEmoji, occur: 10, repeat: 50, },   # Keep track of current/previous emojis
        { fn: genEmoticon, occur: 10, repeat: 0, }, 

        # Modifiers - Repeatable
        { fn: doAsciiShift, occur: 5, repeat, 5 }, # Keep track of current/previous ascii - or have that in the Word/Sentence struct
        { fn: doStutter, occur: 20, repeat: 20, },
        { fn: doCaseShift, occur: 5, repeat: 5, },

        # Modifiers - final/once
        { fn: doLisp, occur: 5 },
        { fn: doUwu, occur: 5 },
    ])
    graph.generate_next_node(amount=3, probabilities)

    # [ Repeat ]
    main(graph)


# note:
#         color = "green" if command else "gray-0"
#         cmd_str = "\"" + str(command) + "\"" if command else "None"
#         Console.puts("\n\t-> {}, {}\n".format(
#             Console.format(cmd_str, [color, "bold" if command else "italic"]),
#             Console.format(pos, [color, "italic"])))


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

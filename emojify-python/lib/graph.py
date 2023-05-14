# todo(joeysapp): Make this an actual linked list (OR GRAPH)
from .utils import Console

# A container that (for now) just gives us the "current" node in the graph
# Later: properties of the graph, etc.
class Graph():    
    def __init__(self, text='', *args, **kwargs):
        self.head = TextNode(text=text)
        self.nodes = { self.head.id: self.head }
        self.path = [self.head.id]
        # todo =================
        # more OOP.. have the Nodes/Verts themselves figure out who they know?
        # self.edges = []...
        # self.edges = [v1][v2] = weight. idk. been forever since graph theory

    def __repr__(self):
        return "Graph(nodes={}, head={})".format(len(self.nodes.keys()), self.head)

    def generate_next(self, amount=10, show=True):
        # Look at self.head and generate N new items from that string, add them to its neighbors
        # Print them out
        candidates = {}
        choice_id = 'a'
        letter_choices = ['a', 'b', 'c']
        if show: Console.method('graph.generate({}) ->\n'.format(self.head))        
        for i in range(0, amount):
            new_id = self.head.id + i
            new_text = self.head.text
            new_text += ' rawr XD' * i
            tmp = TextNode(text=new_text, id=new_id)
            candidates[letter_choices[i%3]] = tmp
            choice_id = tmp.id
            if show: Console.puts('\t[{}] {}\n'.format(letter_choices[i%3], tmp.text))
        if amount > 1:
            choice_id = input('What number would you like to goto: ')
        else:
            choice_id = 0
        print('adding: ', choice_id, candidates)
        self.head.add_neighbor(candidates[choice_id])
        self.nodes.update({ choice_id: candidates[choice_id] })
        self.head = candidates[choice_id]
        


# The Graph will be a collection of TextNodes (entire sentences, etc.)
# Because: we want the gen./mod. to be based upon the entire Text itself, not just individual words.
class TextNode():    
    def __init__(self, text='', id=0, *args, **kwargs):
        self.id = id;
        self.text = text;
        self.neighbors = []; # List of TextNodes vs. list of ids... pythonic.. lel

    def __repr__(self):
        return "TextNode({}, {})".format(self.id, self.text)

    def add_neighbor(self, node):
        self.neighbors.append(node)



# TO CULL



# This is called once per loop
def modify(string):
    next = string
    # Loop through the string
    items = string.split(' ') # Words, words+punctuation, punctuation
    # >>> foo = 'This is, you see! a big @ @ !??? test!'
    # ['This', 'is,', 'you', 'see!', 'a', 'big', '@', '@', '!???', 'test!']


    return next;



class Mutator():
    def __init__(self, *args, **kwargs):
        self.function = None



# Figuring out how to do "dice rolls", etc.
# =========
# v0.1
# Probabilty is out of 100 rolls for the sake of this
# functionMap = {
#     10: getEmoji,
#     20: getAscii,
#     70: get,
# }
# 
# def functionSorter(probability):
#     # "Sorting" here
#     #
#     return functionMap[idx]
# 
# randomRoll = random() * 100
# function = functionSorter(randomRoll);
# function();


# =============
# v0.2

# I kind of want this to handle just arbitrary additions, so 
# I probably need to have the "probability" be related to the bag/list,
# Not a strict percent-chance


# functions = [
#     {
#         # Probability is what? What do these numbers mean
#         function: getEmoji,
#         # 1. Every iteration, getEmoji averages a 10% chance of being called
#         #    - This implies the percent chance it's being rolled is random
#         #    - When we just want a single random item, the dice roll
#         # 2. Soooooo
#         # 2. 
#         min: 0,
#         mean: 10,
#         max: 90,
#         stddev: 10,
#     },
# ]
# 
# def getTextMutator(roll):
#     functions = [
#         { 10: getGarbledText },
#         { 10: getStutterText },
#         { 80: get },
#     ]
#     idx = Math.floor(roll)
#     return functions[idx]
# 
# def getTextAddition(roll):
#     functions = [
#         { 10: getEmoji },
#         { 10: getStutterText },
#         { 80: get },
#     ]
#     idx = Math.floor(roll)
#     return functions[idx]
# 
# # One function
# def getFunction(roll)
#     functions = [
#         # Mutators
#         { 5: getGarbledText },
#         { 5: getStutterText },
#         # Additions
#         { 5: getEmoji },
#         { 5: getStutterText },
#         { 80: get },
#     ]
#     idx = Math.floor(roll)
#     return functions[idx]
# 
# 
# 
# roll = random() * 100
# function = getFunction(roll, functions)
# function()
# 

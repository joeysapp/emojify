from .utils import Console

# Todo: properties of the graph, etc.
class Graph():    
    def __init__(self, text='', *args, **kwargs):
        self.head = TextNode(text=text)
        self.nodes = { self.head.id: self.head }
        self.path = [self.head.id]

    def __repr__(self):
        return "Graph(nodes[{}], head={})".format(len(self.nodes.keys()), self.head)

    def generate_next_text(self, text='', probabilities=None):
        ## I want a function that I can pass an arbitrary number of functions to, with probabilities for each.
        ## I want the function to roll a seeded random number and then execute a function if it matches the probability
        ## 
        ## Maybe I'd like, put each function into a list N times for each function and then randomly pick one? That seems kind of silly
        # What is "Main Loop"?
        text = text
        # Add in generators, modify entire text here
        return text

    def generate_next_node(self, amount=10, probabilities=None, show=True):
        "Look at self.head and generate N new items from that string, add them to its neighbor"
        candidates = {}
        choice_id = 'a'
        letter_choices = ['a', 'b', 'c']
        if show: Console.method('graph.generate({}) ->\n'.format(self.head))        
        for i in range(0, amount):
            # ============================================================
            new_id = self.head.id+i
            new_text = generate_next_text(text=self.head.text, probabilities=probabilities)
            tmp = TextNode(text=new_text, id=new_id)
            # ============================================================
            candidates[letter_choices[i%3]] = tmp
            choice_id = tmp.id
            if show: Console.puts('\t[{}] {}\n'.format(letter_choices[i%3], tmp.text))
        if amount > 1:
            choice_id = input('What number would you like to goto: ')
        else:
            choice_id = 0
        # Note: for now, we're just using this as a linked list lol.
        self.head.add_neighbor(candidates[choice_id])
        self.nodes.update({ choice_id: candidates[choice_id] })
        self.head = candidates[choice_id]
        
# The Graph will be a collection of TextNodes (entire sentences, etc.)
# -- becase: we want the gen./mod. to be based upon the entire Text itself, not just individual words.
class TextNode():    
    def __init__(self, text='', id=0, *args, **kwargs):
        self.id = id;
        self.text = text;
        self.neighbors = []; # Python, so just append actual 'references'

    def __repr__(self):
        return "TextNode({}, {})".format(self.id, self.text)

    def add_neighbor(self, node):
        self.neighbors.append(node)


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

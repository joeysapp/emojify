from .utils import Console

# Todo: properties of the graph, etc.
class Graph():    
    def __init__(self, value='', *args, **kwargs):
        self.head = Node(value)
        self.nodes = { self.head.id: self.head }
        self.path = [self.head.id]

    def __repr__(self):
        return "Graph(nodes[{}], head={})".format(len(self.nodes.keys()), self.head)

    def generate_next_node(self, amount=10, probabilities=None, show=True):
        "Look at self.head and generate N Nodes from that string, [currently] ask user to pick one"
        candidates = []
        if show: Console.method('graph.generate_next_node({}) ->\n'.format(self.head))        
        for i in range(0, amount):
            # ============================================================
            new_id = self.head.id+i # nodes probably should have a hash function eventually
            new_value = probabilities.next(self.head)
            tmp = Node(value=new_text, id=new_id)
            # ============================================================
            # Simple user-input choice dealio right now
            candidates.append(tmp)
            if show: Console.puts('\t[#{}] {}\n'.format(letter_choices[i%3], tmp.text))
        choice_idx = False
        while choice_idx not in candidates and amount > 1:
            choice_idx = int(input('Please pick a generation: '))
        new_node = candidates[choice_idx or 0]
        # Note: for now, we're just using this as a linked list lol.
        self.head.add_neighbor(new_node)
        self.nodes.update({ [new_node.id]: new_node })
        self.head = new_node
        
# The Graph will be a collection of Node, which themselves have a Type
# -- becase: we want the gen./mod. to be based upon the entire Text itself, not just individual words.
class Node():    
    def __init__(self, value=None, id=0, neighbors=[], *args, **kwargs):
        self.value = value;
        self.id = id;
        self.neighbors = []; # Python, so just append actual 'references'

    def __repr__(self):
        return "Node({}, {})".format(self.id, self.text)

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

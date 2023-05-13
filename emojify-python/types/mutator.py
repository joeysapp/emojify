
class Mutator():
    def __init__(self, *args, **kwargs):
        self.function = None



# =========
# v0.1
# Probabilty is out of 100 rolls for the sake of this
functionMap = {
    10: getEmoji,
    20: getAscii,
    70: get,
}

def functionSorter(probability):
    # "Sorting" here
    #
    return functionMap[idx]

randomRoll = random() * 100
function = functionSorter(randomRoll);
function();


# =============
# v0.2

# I kind of want this to handle just arbitrary additions, so 
# I probably need to have the "probability" be related to the bag/list,
# Not a strict percent-chance


functions = [
    {
        # Probability is what? What do these numbers mean
        function: getEmoji,
        # 1. Every iteration, getEmoji averages a 10% chance of being called
        #    - This implies the percent chance it's being rolled is random
        #    - When we just want a single random item, the dice roll
        # 2. Soooooo
        # 2. 
        min: 0,
        mean: 10,
        max: 90,
        stddev: 10,
    },
]

def getTextMutator(roll):
    functions = [
        { 10: getGarbledText },
        { 10: getStutterText },
        { 80: get },
    ]
    idx = Math.floor(roll)
    return functions[idx]

def getTextAddition(roll):
    functions = [
        { 10: getEmoji },
        { 10: getStutterText },
        { 80: get },
    ]
    idx = Math.floor(roll)
    return functions[idx]

# One function
def getFunction(roll)
    functions = [
        # Mutators
        { 5: getGarbledText },
        { 5: getStutterText },
        # Additions
        { 5: getEmoji },
        { 5: getStutterText },
        { 80: get },
    ]
    idx = Math.floor(roll)
    return functions[idx]



roll = random() * 100
function = getFunction(roll, functions)
function()

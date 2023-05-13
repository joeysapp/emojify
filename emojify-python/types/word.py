class WordType():
    def __init__(self, *args, **kwargs):
        self.type = ''

    def __repr__(self):
        return "WordType({})".format(self.__dict__)


class Word():
    def __init__(self, *args, **kwargs):
        self.source = ''
        self.history = []
        # TODOS
        self.sentiment = []
        # Actions (or functions/mutators/decorators) that have been done to it?
        self.actions = []

    def __repr__(self):
        return "Word({})".format(self.__dict__)




import random

class SeededRandom(random.Random):
    '''
        Random class wrapper, provided a seeded random number generator
    '''
    def __init__(self, seed=0):
        random.Random.__init__(self)
        self.seed(seed)

Random = SeededRandom()
from .utils import is_pythagorean_triple

class Triple:
    '''
    Class representing a pythagorean triple.
    '''

    def __init__(self, x, y, r):
        '''
        Instantiate a Triple object
        '''
        self.x, self.y, self.r = x, y, r


a = Triple(3, 4, 5)

print(type(a) == Triple)
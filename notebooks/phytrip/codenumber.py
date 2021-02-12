from .triple import Triple

class CodeNumber:
    def __init__(self, c, d):
        '''
        Class to represent code numbers.
        '''
        self.c, self.d = c, d

    def __str__(self):
        '''
        A string representation of a code number.
        '''
        return f'CodeNumber{self.get()}'
    
    def __repr__(self):
        '''
        A representation of a code number.
        '''
        return f'CodeNumber{self.get()}'


    def get(self):
        '''
        Get a tuple of elements.
        '''
        return self.c, self.d

    def triple(self):
        # Triples pp. 67
        '''
        Return a triple corresponding to the code numbers.
        '''
        c, d = self.get()
        return Triple(c * c - d * d, 2 * c * d, c * c + d * d)
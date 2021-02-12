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
from math import gcd

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

    def scale_mult(self, s):
        '''
        Returns a new codenumber with the elements multiplied by s.
        '''
        (c, d) = self.get()
        return CodeNumber(c * s, d * s)

    def scale_div(self, s):
        '''
        Returns a new codenumber with the elements divided by s.
        '''
        (c, d) = self.get()
        return CodeNumber(c / s, d / s)

    def scale_common(self):
        '''
        Returns a new codenumber with the elements divided by their common factor.
        Only applies to perfect, integer, codenumbers.
        '''
        if not self._is_perfect():
            (c, d) = self.get()
            return CodeNumber(c, d)
        else:
            (c, d) = self._make_perfect().get()
            cd = gcd(c, d)
            return CodeNumber(c / cd, d / cd)._make_perfect()
    
    def _is_perfect(self):
        (c, d) = self.get()
        return (c, d) == (int(c), int(d))

    def _make_perfect(self):
        (c, d) = self.get()
        (c, d) = (int(c), int(d))
        return CodeNumber(c, d)
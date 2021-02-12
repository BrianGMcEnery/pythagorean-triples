from math import gcd

class CodeNumber:
    '''
    Class to represent code numbers.
    '''

    def __init__(self, c, d):
        '''
        Initialise a code number.
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

    def add(self, b):
        # Triples pp. 69
        '''
        Return the sum of two codenumbers
        '''
        (c, d) = self.get()
        (cb, db) = b.get()
        return CodeNumber(c * cb - d * db, d * cb + c * db)

    def sub(self, b):
        # Triples pp. 69
        '''
        Return the difference of two codenumbers.
        '''
        (c, d) = self.get()
        (cb, db) = b.get()
        return CodeNumber(c * cb + d * db, d * cb - c * db)

    def complement(self):
        # Triples pp. 71
        '''
        Return the complementary codenumber.
        '''
        (c, d) = self.get()
        return CodeNumber(c + d, c - d)

    def supplement(self):
        # Triples pp. 71
        '''
        Return the supplementary codenumber.
        '''
        (c, d) = self.get()
        return CodeNumber(d, c)

    @staticmethod
    def quadrant_angle(angle):
        # Triples pp. 72
        '''
        Returns a new codenumber corresponding to the quadrant angles,
        [0, 90, 180, 270, 360].
        '''
        quadrant_codenumbers = {
            0: CodeNumber(1, 0),
            90: CodeNumber(1, 1),
            180: CodeNumber(0, 1),
            270: CodeNumber(1, -1),
            360: CodeNumber(1, 0),
        }
        if angle not in quadrant_codenumbers.keys():
            raise ValueError(f'{angle} is not a quadrant angle.')
        else:
            return quadrant_codenumbers[angle]


    
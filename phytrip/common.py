from .triple import Triple
from .codenumber import CodeNumber

def codenumber(t):
        # Triples pp. 68
        '''
        Return a codenumber corresponding to the triple
        '''
        (x, y, r) = t.get()
        (c, d) = x + r, y
        return CodeNumber(c, d)

def triple(cn):
        # Triples pp. 67
        '''
        Return a triple corresponding to the code numbers.
        '''
        c, d = cn.get()
        return Triple(c * c - d * d, 2 * c * d, c * c + d * d)

 
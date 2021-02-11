from math import isclose

def is_pythagorean_triple(x, y, r):
    '''
    Returns true if x**2 + y**2 = r**2.
    '''
    isclose(x ** 2 + y ** 2, r ** 2)
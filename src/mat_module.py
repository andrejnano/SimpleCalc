import math
import numbers


def add ( A , B ):
    if ( not isinstance(A, numbers.Real) and isinstance(B, numbers.Real)):
        raise ValueError('Number passed to function add is not float')
    else:
        return A + B
    

def sub ( A , B ):
    if ( not isinstance(A, numbers.Real) and isinstance(B, numbers.Real)):
        raise ValueError('Number passed to function add is not float')
    else:
        return A - B

def mul ( A , B ):
    if ( not isinstance(A, numbers.Real) and isinstance(B, numbers.Real)):
        raise ValueError('Number passed to function add is not float')
    else:
        return A * B


def div ( A , B ):
    if ( not isinstance(A, numbers.Real) and isinstance(B, numbers.Real)):
        raise ValueError('Number passed to function add is not float')
    else:
        return A / B

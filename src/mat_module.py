import math
import numbers


def add ( A , B ):
    if ( not (isinstance(A, numbers.Real) and isinstance(B, numbers.Real))):
        raise ValueError('Argument passed to function add is not float')
    else:
        return A + B
    

def sub ( A , B ):
    if ( not (isinstance(A, numbers.Real) and isinstance(B, numbers.Real))):
        raise ValueError('Argument passed to function sub is not float')
    else:
        return A - B

def mul ( A , B ):
    if ( not (isinstance(A, numbers.Real) and isinstance(B, numbers.Real))):
        raise ValueError('Argument passed to function mul is not float')
    else:
        return A * B


def div ( A , B ):
    if ( not (isinstance(A, numbers.Real) and isinstance(B, numbers.Real))):
        raise ValueError('Argument passed to function div is not float')
    else:
        return A / B

def sqrt ( A ):
    if ( not (isinstance(A, numbers.Real) )):
        raise ValueError('Argument passed to function sqrt is not float')
    else:
        return math.sqrt(A)


def factorial( A ):
    if ( not (isinstance(A, numbers.Integral) )):
        raise ValueError('Argument passed to function factorial is not int')
    A = int(A)
    result = A
    A -= 1
    while ( A > 1 ) :
        result *= A
        A -= 1
    return result 
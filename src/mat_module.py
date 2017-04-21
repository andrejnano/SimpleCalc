#!/bin/python

import math
import numbers

# spusti funkciu evaluate pre pocitanie
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

def root ( A,B ):
    if ( not (isinstance(A, numbers.Real) and isinstance(B, numbers.Real))):
        raise ValueError('Argument passed to function root is not float')
    else:
        return B**(1.0/A)


def factorial( A ):
    if ( not (A).is_integer()):
        raise ValueError('Argument passed to function factorial is not int')
    if ( A < 0):
        raise ValueError('Factorial from negative number')
    A = int(A)
    result = A
    A -= 1
    while ( A > 1 ) :
        result *= A
        A -= 1
    return float(result) 

def sin( A ):
    if ( not (isinstance(A, numbers.Real) )):
        raise ValueError('Argument passed to function sin is not float')
    else:
        return math.sin(A)

def cos( A ):
    if ( not (isinstance(A, numbers.Real) )):
        raise ValueError('Argument passed to function cos is not float')
    else:
        return math.cos(A)

def tan( A ):
    if ( not (isinstance(A, numbers.Real) )):
        raise ValueError('Argument passed to function tan is not float')
    else:
        return math.tan(A)

def log( A ):
    if ( not (isinstance(A, numbers.Real) )):
        raise ValueError('Argument passed to function log is not float')
    else:
        return math.log(A)

def isnum( char ):
    if (ord(char) > 46 and ord(char) < 58):
        return 1
    else:
        return 0

# funkcia ktoru treba spustit pre pocitanie
def evaluate( string ):
    while( string.find("(") != -1 ):
        l_idx = lbidx(string)
        r_idx = rbidx(string)
        string = string[:l_idx] +calculate(string[l_idx+1:r_idx]) + string[r_idx+1:]
    result = calculate(string)
    if(result[0] is "+"):
        return result[1:]
    else:
        return result 


def find_nan( string ):
    i = 0
    for c in string:
        if not ((ord(c) > 47 and ord(c) < 58) or c is '.' or c is 'e' ):
            return i
        if(c is "e"):
            return i + find_nan(string[i+2:]) + 2
        i += 1
    return len(string)

def trigonFunc(string, sign,func):
    while ( string.find(sign) > -1):
         lidx = string.find(sign)
         ridx = lidx + 4 + find_nan(string[lidx+4:])
         string = string[:lidx] + (str("%.12f" % func(float(string[lidx+3:ridx]))).rstrip('0').rstrip('.')) + string[ridx:]
         break
    print(string)
    
    return string

def calcFactorSqrt( string ):
    sqr_sindex = string.rfind("\xe2\x88\x9a")
    while (sqr_sindex >= 0):
        if (isnum(string[sqr_sindex-1])):
            string = string[:sqr_sindex]  + string[sqr_sindex:]
            sqr_sindex += 1
        sqr = string[sqr_sindex + 2:]
        sqr_eindex = find_nan(sqr) 
        sqr = sqr[:sqr_eindex]
        second = sqr
        tmpstr = string[:sqr_sindex -1]
        sqr_sidx = find_nan(tmpstr[::-1])
        print(sqr_sidx)
        first = string[sqr_sindex-sqr_sidx-1:sqr_sindex-1]
        print(first)
        if(first is ""):
            first = "2"
        sqr = str("%.12f" % root(float(first),float(second))).rstrip('0').rstrip('.')
        print"this is it"
        print(string[:sqr_sindex-sqr_sidx-2])
        string =  string[:sqr_sindex-sqr_sidx - 1] + sqr + string[sqr_sindex + sqr_eindex +2:]
        sqr_sindex = string.rfind("\xe2\x88\x9a")

    fac_eindex = string.find("!")
    while (fac_eindex >= 0):
        fac = string[:fac_eindex]
        fac_sindex = find_nan(fac[::-1]) 
        fac = fac[fac_eindex - fac_sindex:fac_eindex]
        fac = str("%.12f" % factorial(float(fac))).rstrip('0').rstrip('.')
        string =  string[:fac_eindex - fac_sindex] + fac + string[fac_eindex + 1:]
        fac_eindex = string.find("!")

    string = trigonFunc(string,"sin",sin)
    string = trigonFunc(string,"cos",cos)
    string = trigonFunc(string,"tan",tan)
    string = trigonFunc(string,"log",log)
    #  break
    # while ( string.find("cos(") > -1):
    # while ( string.find("tan(") > -1):
    return string

def determineSign( string ):
    minuses=1
    i=0
    l = len(string)
    if(l == -1):
        return "+"
    # tmpstr=""
    while((string[i] is "+" or string[i] is "-" or string[i] is " ") and i < l ):
        if(string[i] is "-"):
            minuses += 1
        i += 1
    if ( minuses % 2 == 0):
        string = "-" + string[i:]
    else:
        string = "+" + string[i:]
    return string

def lbidx( string ):
    l_idx = 0
    i = 0
    if (string.find("(") == -1 or string.find(")") == -1):
        return -1 
    for c in string:
        if (c is "("):
            l_idx = i
        if(c is ")"):
            break
        i+=1
    return l_idx


def rbidx( string ):
    l_idx = 0
    i = 0
    if (string.find("(") == -1 or string.find(")") == -1):
        return -1 
    for c in string:
        if (c is "("):
            l_idx = i
        if(c is ")"):
            break
        i+=1
    return i

def calcSum( string ):
    # nacitaj prve cislo
    # vyhodnot znamienko
    while(string is not ""):
        string = determineSign(string)
        i = 1 + find_nan(string[1:])
        first = string[:i]
        string = string[i:]
        if(string is ""):
            return first
        string = determineSign(string)
        i = 1 + find_nan(string[1:])
        second =  string[:i]
        string = str("%.12f" %  add(float(first),float(second)) + string[i:]).rstrip('0').rstrip('.')
    return string

def calcBasicOperations( string, sign, operation ):
    # sign index je index znamienka
    sign_index = string.find(sign)
    while (sign_index >= 0):
        # index praveho konca prveho argumentu funkcie operation
        FNumIdx_r = sign_index - 1
        while (string[FNumIdx_r] is ' '):
            FNumIdx_r -= 1
        FNumIdx_l = find_nan(string[FNumIdx_r::-1])
        FNumIdx_r += 1
        # bude prvy argument do funkcie operation
        FNum = string[FNumIdx_r - FNumIdx_l :FNumIdx_r]
        FNumIdx_ll = FNumIdx_r - FNumIdx_l
        # print(string[FNumIdx_r - FNumIdx_l - 1])
            
        if (string[FNumIdx_r - FNumIdx_l - 1] is "-" or string[FNumIdx_r - FNumIdx_l - 1] is "+" ):
            FNumIdx_ll = FNumIdx_r - FNumIdx_l - 1
            FNumIdx_r = find_nan(string[FNumIdx_ll +1 :])
            # print(string[FNumIdx_r - FNumIdx_l - 1:FNumIdx_r+2])
            FNum = string[FNumIdx_ll :FNumIdx_ll + FNumIdx_r+1]
                        

        SNumIdx_l = sign_index + 1
        SNumIdx_r = find_nan(string[SNumIdx_l:])
        
        # FNumIdx_r += 1
        SNum = string[SNumIdx_l:SNumIdx_l + SNumIdx_r]
        
        if (string[SNumIdx_l] is "-" or string[SNumIdx_l] is "+" ):
            SNumIdx_l += 1
            SNumIdx_r = find_nan(string[SNumIdx_l:])
            SNum = string[SNumIdx_l-1:SNumIdx_l + SNumIdx_r]
        
        if(SNum is ""):
            break

        result = str("%.12f" % operation(float(FNum),float(SNum))).rstrip('0').rstrip('.')
        if(result[0] is not "-"):
            string = string[:FNumIdx_ll] +"+"+ result + string[SNumIdx_l + SNumIdx_r:]
        else:
            string = string[:FNumIdx_ll] + result + string[SNumIdx_l + SNumIdx_r:]
        sign_index = string.find(sign)
    return string

    
# vypocita jednoduchy vyraz zlozeny zo zakladnych operacii + - * / sqrt !
def calculate( string ):
    string = calcFactorSqrt(string)
    string = calcBasicOperations( string , "/" , div )
    string = calcBasicOperations( string , "*" , mul )
    string = calcSum(string)
    return string



# spusti funkciu evaluate pre pocitanie
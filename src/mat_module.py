#!/bin/python

##
# @file mat_module.py
# @author Peter Marko 
# @package mat_module
# @date 22 April 2017
# @brief documentation of source code of mat_module which will be used in main.py 
# 
# this module defines functions for evaluation of string as mathematical operation
#

import math
import numbers

##
# ...
# Function adds A and B
# @param A,B
# @pre A and B are float numbers
# @return sum of A and B

def add ( A , B ):
    if ( not (isinstance(A, numbers.Real) and isinstance(B, numbers.Real))):
        raise ValueError('Argument passed to function add is not float')
    else:
        return A + B

##
# Function muls A and B
# @param A,B
# @pre A and B are float numbers
# @return multiplication of A and B
def mul ( A , B ):
    if ( not (isinstance(A, numbers.Real) and isinstance(B, numbers.Real))):
        raise ValueError('Argument passed to function mul is not float')
    else:
        return A * B

##
# Function divides A by B
# @param A,B
# @pre A and B are float numbers
# @return A divided by B
def div ( A , B ):
    if ( not (isinstance(A, numbers.Real) and isinstance(B, numbers.Real))):
        raise ValueError('Argument passed to function div is not float')
    else:
        return A / B


##
# Function calculates A-th root of number B
# @param A,B
# @pre A and B are float numbers
# @return A-th root of B
def root ( A,B ):
    if ( not (isinstance(A, numbers.Real) and isinstance(B, numbers.Real))):
        raise ValueError('Argument passed to function root is not float')
    else:
        return B**(1.0/A)


##
# Function calculates factorial of A
# @param A
# @pre A is float but natural number
# @return factorial of A 
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


##
# Function finds sine of A
# @param A
# @pre A is float number
# @return sine of A
def sin( A ):
    if ( not (isinstance(A, numbers.Real) )):
        raise ValueError('Argument passed to function sin is not float')
    else:
        return math.sin(A)


##
# Function finds cosine of A
# @param A
# @pre A is float number
# @return cosine of A
def cos( A ):
    if ( not (isinstance(A, numbers.Real) )):
        raise ValueError('Argument passed to function cos is not float')
    else:
        return math.cos(A)


##
# Function finds tangent of A
# @param A
# @pre A is float number
# @return tangent of A
def tan( A ):
    if ( not (isinstance(A, numbers.Real) )):
        raise ValueError('Argument passed to function tan is not float')
    else:
        return math.tan(A)


##
# Function finds natural logarithm of A
# @param A
# @pre A is float number
# @return natural logarithm of A
def log( A ):
    if ( not (isinstance(A, numbers.Real) )):
        raise ValueError('Argument passed to function log is not float')
    else:
        return math.log(A)

##
# Function calculates value of A to the power of B
# @param A base
# @param B exponent
# @pre 
# A and B are float numbers <br>
# B is natural whole number
# @return A to the power B
def power( A , B ):
    if ( not (isinstance(A, numbers.Real) and isinstance(B, numbers.Real))):
        raise ValueError('Argument passed to function pow is not float')
    if ( B < 0 or not (B).is_integer() or B == 0):
        raise ValueError('Power to unnatural exponent')
    else:
        result = 1
        B = int(B)
        for i in range(B):
            result *= A
        return result

##
# Function determines whether character passed is digit
# @param char
# @pre char is a string of length 1
# @return
# -# 1 if char is digit
# -# if char is not digit 0
def isnum( char ):
    if (ord(char) > 47 and ord(char) < 58):
        return 1
    else:
        return 0

##
# Function lbidx = left bracket index determines last index at which is "(" before ")"
# @param string
# @pre string is instance of data type str
# @return
# -# -1 if "(" or ")" not found 
# -# else  last index at which is "(" before ")"
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

##
# Function rbidx = right bracket index determines first index at which is ")" after "("
# @param string
# @pre string is instance of data type str
# @return
# -# -1 if "(" or ")" not found
# -# else  first index at which is ")" after "("
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

##
# Function evaluates string as it is colection of mathematical operations 
# @param string
# @pre string is instance of data type str
# @return result of operations from input string transformed in string format
# @post error raised if not correct mathematical operation passed
def evaluate( string ):
    if(string.find(" ") > -1):
        raise ValueError('String contains space')
    while( string.find("(") != -1 ):
        l_idx = lbidx(string)
        r_idx = rbidx(string)
        if(len(string[r_idx+1:]) > 0 and isnum(string[r_idx+1])):
            print(string)
            raise ValueError('Number directly after bracket')
        if(isnum(string[l_idx-1]) and l_idx > 0):
            string = string[:l_idx] +"*"+calculate(string[l_idx+1:r_idx]) + string[r_idx+1:]  
        else:  
            string = string[:l_idx] +calculate(string[l_idx+1:r_idx]) + string[r_idx+1:]
    result = calculate(string)
    result = float(result)
    result = "%g" % result

    if(result[0] is "+"):
        return result[1:]
    if(result == "-0"):
        return "0"
    else:
        return result 

##
# Function finds index wher number stored in string ends 
# @param string
# @pre string is instance of data type str
# @return int end index of number in string
def findEndOfNum( string ):
    i = 0
    for c in string:
        if not ((ord(c) > 47 and ord(c) < 58) or c is '.' or string[i:i+2].find('+e') > -1 or string[i:i+2].find('-e') > -1 or c is "e"):
            return i
        if(c is "e"):
            return i + findEndOfNum(string[i+2:]) + 2
        i += 1
    return i

##
# Function calculates trigonometric functions as sin cos tan or log 
# @param 
# string , sign is string containing sin cos tan or log - depends on operation
# @pre 
# string is instance of data type str <br> 
# sign is instance of data type str <br>
# func is pointer to function sin cos tan or log
# @return string with substituted values of function
def trigonFunc(string, sign,func):
    while ( string.find(sign) > -1):
         lidx = string.find(sign)
         ridx = lidx + 4 + findEndOfNum(string[lidx+4:])
         string = string[:lidx] + (str("%.12f" % func(float(string[lidx+3:ridx]))).rstrip('0').rstrip('.')) + string[ridx:]
         break
    
    return string

##
# Function calculates values of roots,factorials and pi and substitues them into original string 
# @param string
# @pre string is instance of data type str 
# @return string with substituted values of roots and factorials
def calcFactorSqrt( string ):
    # starting index of number under the root
    
    piidx=string.find('\xcf\x80')
    
    while(piidx > -1):
        if(len(string[piidx:])>2 and isnum(string[piidx+2])):
            raise ValueError('Number directly after pi')
        if(isnum(string[piidx-1]) and piidx > 0):
            string = string[:piidx]+"*3.14159265359"+string[piidx+2:]            
        else:
            string = string[:piidx]+"3.14159265359"+string[piidx+2:]
        piidx=string.find('\xcf\x80')
    
    sqr_sindex = string.rfind("\xe2\x88\x9a")
    # searching for starting and ending indices and transforming the number from str to float
    while (sqr_sindex >= 0):
        if (isnum(string[sqr_sindex-1])):
                sqr_sindex += 1
        sqr = string[sqr_sindex + 2:]
        if(sqr[0] is "+" or sqr[0] is "-" ):
            sqr_eindex = findEndOfNum(sqr[1:]) + 1 
        else:
            sqr_eindex = findEndOfNum(sqr) 
        sqr = sqr[:sqr_eindex]
        second = sqr
        tmpstr = string[:sqr_sindex -1]
        sqr_sidx = findEndOfNum(tmpstr[::-1])
        first = string[sqr_sindex-sqr_sidx-1:sqr_sindex-1]
        if(first is ""):
            first = "2"
        sqr = str("%.12f" % root(float(first),float(second))).rstrip('0').rstrip('.')
        string =  string[:sqr_sindex-sqr_sidx - 1] + sqr + string[sqr_sindex + sqr_eindex +2:]
        sqr_sindex = string.rfind("\xe2\x88\x9a")

    # searching for starting and ending indices and transforming the number from str to float
    fac_eindex = string.find("!")
    while (fac_eindex >= 0):
        fac = string[:fac_eindex]
        fac_sindex = findEndOfNum(fac[::-1]) 
        fac = fac[fac_eindex - fac_sindex:fac_eindex]
        fac = str("%.12f" % factorial(float(fac))).rstrip('0').rstrip('.')
        string =  string[:fac_eindex - fac_sindex] + fac + string[fac_eindex + 1:]
        fac_eindex = string.find("!")

    string = trigonFunc(string,"sin",sin)
    string = trigonFunc(string,"cos",cos)
    string = trigonFunc(string,"tan",tan)
    string = trigonFunc(string,"log",log)
    return string

##
# Function function determines sign of number from "before number" substring which starts with "-" or "+"  
# @param string
# @pre string is instance of data type str and starts with "+" or "-" 
# @return original string with with calculated and substitued sign at the begining

def determineSign( string ):
    minuses=1
    i=0
    l = len(string)
    if(l == 0):
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

##
# Function evaluates value of string containing only "-" or "+" operations  
# @param string
# @pre string is instance of data type str and contains no other operations than "+" or "-" 
# @return calculated value converted to str
def calcSum( string ):
    # nacitaj prve cislo
    # vyhodnot znamienko
    while(string is not ""):
        string = determineSign(string)
        i = 1 + findEndOfNum(string[1:])
        first = string[:i]
        string = string[i:]
        if(string is ""):
            return first
        string = determineSign(string)
        i = 1 + findEndOfNum(string[1:])
        second =  string[:i]
        string = str("%.12f" %  add(float(first),float(second)) + string[i:]).rstrip('0').rstrip('.')
    return string

##
# ...
# Function substitues value of "*" or "/" operations to original string  
# @param 
# string <br>
# sign is "*" or "/" <br>
# operation is pointer to func
# @pre 
# string is instance of data type str <br>
# sign is instance of data type str and can contain just "*" or "/" <br>
# operation is pointer tu function with two argumants which should be used to evaluate operation
# @return calculated value converted to str substitued to original string
def calcBasicOperations( string, sign, operation ):
    # sign index is position of sign "*" or "/"
    sign_index = string.find(sign)
    while (sign_index >= 0):
        # index right end of first argument of function operation
        FNumIdx_r = sign_index - 1
        while (string[FNumIdx_r] is ' '):
            FNumIdx_r -= 1
        FNumIdx_l = findEndOfNum(string[FNumIdx_r::-1])
        FNumIdx_r += 1
        # will be first arg to func operation
        FNum = string[FNumIdx_r - FNumIdx_l :FNumIdx_r]
        FNumIdx_ll = FNumIdx_r - FNumIdx_l
            
        if (string[FNumIdx_r - FNumIdx_l - 1] is "-" or string[FNumIdx_r - FNumIdx_l - 1] is "+" ):
            FNumIdx_ll = FNumIdx_r - FNumIdx_l - 1
            FNumIdx_r = findEndOfNum(string[FNumIdx_ll +1 :])
            FNum = string[FNumIdx_ll :FNumIdx_ll + FNumIdx_r+1]
                        

        SNumIdx_l = sign_index + 1
        SNumIdx_r = findEndOfNum(string[SNumIdx_l:])
        
        SNum = string[SNumIdx_l:SNumIdx_l + SNumIdx_r]
        
        if (string[SNumIdx_l] is "-" or string[SNumIdx_l] is "+" ):
            SNumIdx_l += 1
            SNumIdx_r = findEndOfNum(string[SNumIdx_l:])
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

##
# Function evaluates simple expression consisting only from operations ^ * / root !   
# @param string
# @pre string is instance of data type str 
# @return calculated value converted to str substitued to original string   
def calculate( string ):
    string = calcFactorSqrt(string)
    string = calcBasicOperations( string , "^" , power )
    string = calcBasicOperations( string , "/" , div )
    string = calcBasicOperations( string , "*" , mul )
    string = calcSum(string)
    return string



# spusti funkciu evaluate pre pocitanie

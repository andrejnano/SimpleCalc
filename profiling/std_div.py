#!/bin/python
import sys
sys.path.append('../src')
import mat_module
import cProfile

def std_div():
    data = []
    N="0"
    sum = "0"
    for line in sys.stdin:
        data.append(line[:-1])
        sum = mat_module.evaluate(line[:-1]+"+"+sum)
        N = mat_module.evaluate("1"+"+"+N)
    avg = mat_module.evaluate("("+sum+")/"+N)
    j="0"
    sum = "0"
    for i in data:
        sum = mat_module.evaluate(sum+"+"+"("+data[int(j)] +"-"+ avg+")"+"^2")
        j = mat_module.evaluate("1+"+j)
    string = '\xe2\x88\x9a('+sum+"/(" + N + "-1))"
    S = mat_module.evaluate(  string  )
    print(S)
    return S
cProfile.run("std_div()")

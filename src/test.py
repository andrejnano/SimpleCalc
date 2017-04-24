#!/bin/python
# -*- coding: <unicode> -*-
import pytest
import mat_module

def test_add():
# klasicke porovnanie vysledkov pomocou assertu
    assert mat_module.add(1.0,3.14159265358) == 4.14159265358 
    assert mat_module.add(1,0) == 1
    assert mat_module.add(42,-42) == 0
    assert mat_module.add(-42,-42) == -84
# testovanie vynimiek
    with pytest.raises(Exception):
        mat_module.add(-42,"str")
    with pytest.raises(Exception):
        mat_module.add("str","ing")
    with pytest.raises(Exception):
        mat_module.add([1,2],[3,4])
    with pytest.raises(Exception):
        mat_module.factorial()
    with pytest.raises(Exception):
        mat_module.factorial(-1.54,59,0.3)

def test_mul():
    assert mat_module.mul(6.022e+23,3.14159265358) == 1.891867095985876e+24 
    assert mat_module.mul(99999.1534564,0) == 0
    assert mat_module.mul(42,-0) == 0
    assert mat_module.mul(-42,-42) == 1764
    with pytest.raises(Exception):
        mat_module.mul(-2e-54,"str")
    with pytest.raises(Exception):
        mat_module.mul("str","ing")
    with pytest.raises(Exception):
        mat_module.mul([-0.451,2.77],[3.4,64.4])
    with pytest.raises(Exception):
        mat_module.factorial()
    with pytest.raises(Exception):
        mat_module.factorial(-4.2,4.2,89)


def test_div():
    assert mat_module.div(6.022e+23,3.14159265358) == 1.916862134604763e+23 
    assert mat_module.div(-99999.1534564,-456) == 219.29638915877194
    assert mat_module.div(2,2) == 1
    assert mat_module.div(-4.2,-42) == 0.1
    assert mat_module.div(0,-42) == 0
    with pytest.raises(Exception):
        mat_module.div(0,0)
    with pytest.raises(Exception):
        mat_module.div(1,0)
    with pytest.raises(Exception):
        mat_module.mul("str","ing")
    with pytest.raises(Exception):
        mat_module.mul([-0.451,2.77],[3.4,64.4])
    with pytest.raises(Exception):
        mat_module.factorial()
    with pytest.raises(Exception):
        mat_module.factorial(-1.54,59,0.3)
    with pytest.raises(Exception):
        mat_module.factorial(99,456.2,"abc")


def test_root():
    assert mat_module.root(2,6.022e+23) == 776015463763.4485 
    assert mat_module.root(2,25) == 5
    assert mat_module.root(2.5,7) == 2.17790642448278
    assert mat_module.root(0.3,2) == 10.079368399158986 
    assert mat_module.root(2,2) == 1.4142135623730951
    with pytest.raises(Exception):
        mat_module.root(2,-2)
    with pytest.raises(Exception):
        mat_module.root("str","ing")
    with pytest.raises(Exception):
        mat_module.root([-0.451,2.77,3.4,64.4])
    with pytest.raises(Exception):
        mat_module.factorial()
    with pytest.raises(Exception):
        mat_module.factorial(-1.54,3)


def test_factorial():
    assert mat_module.factorial(5.0) == 120 
    assert mat_module.factorial(15.0) == 1307674368000
    assert mat_module.factorial(0.0) == 0
    assert mat_module.factorial(2.0) == 2
    with pytest.raises(Exception):
        mat_module.factorial(-2.0)
    with pytest.raises(Exception):
        mat_module.factorial("str","ing")
    with pytest.raises(Exception):
        mat_module.factorial(64.4)
    with pytest.raises(Exception):
        mat_module.factorial(1,2)
    with pytest.raises(Exception):
        mat_module.factorial()


def test_power():
    assert (mat_module.power(5.2,3.0) - 140.608 < 0.0001)
    assert (mat_module.power(15.34,4.0) - 55373.4316 < 0.0001)
    assert (mat_module.power(3.3,5.0) - 391.35393 < 0.0001)
    assert (mat_module.power(0.9,7.0) - 0.4782969 < 0.0001)
    assert (mat_module.power(0.9,1.0) - 0.9 < 0.0001)
    with pytest.raises(Exception):
        mat_module.power(-2.0,0.1)
    with pytest.raises(Exception):
        mat_module.power(0.0,0)
    with pytest.raises(Exception):
        mat_module.power(64.4,-1)
    with pytest.raises(Exception):
        mat_module.power(1.5,-2.1)
    with pytest.raises(Exception):
        mat_module.power(0.0,0.0)
    with pytest.raises(Exception):
        mat_module.power(-1.0,-1.0)


def test_evaluate():
    assert mat_module.evaluate("\xe2\x88\x9a81") == "9"
    assert mat_module.evaluate("2.1*(4\xe2\x88\x9a81)-4!") == "-17.7"
    assert mat_module.evaluate("6!") == "720" 
    assert mat_module.evaluate("10/4.654") == "%g" % 2.148689299527
    assert mat_module.evaluate("7.32*-1.2122") == "%g" % -8.873304
    assert mat_module.evaluate("2^3!") == "%g" %  64
    assert mat_module.evaluate("(1+7.21-4)/(3*2.84-7)") == "%g" %  2.76973684211
    assert mat_module.evaluate("6.022e23-6.022e22") == "%g" %  5.4198e+23
    assert mat_module.evaluate("(1+sin(2-cos(-7))-7.81)") == "%g" %  -5.86225307094
    assert mat_module.evaluate("(1+log(2-tan(-7))-7.81)") == "%g" %  -5.75518357386
    assert mat_module.evaluate("log(2)") == "%g" %  0.69314718056   
    assert mat_module.evaluate("log(2)*sin(2)") == "%g" %  0.63027694769
    assert mat_module.evaluate("log(2)*(sin(2))^3") == "%g" %  0.521126727
    assert mat_module.evaluate("(-2)^3") == "%g" %  -8
    assert mat_module.evaluate("sin(-\xcf\x80/2)") == "%g" %  -1
    assert mat_module.evaluate("cos(-\xcf\x80/2)") == "%g" %  0
    assert mat_module.evaluate("((cos(-\xcf\x80/2)+1-1)/1)^2") == "%g" %  0
    

    with pytest.raises(Exception):
        assert mat_module.evaluate("6.32!")
    with pytest.raises(Exception):
        assert mat_module.evaluate("6.32^-1")
    with pytest.raises(Exception):
        assert mat_module.evaluate("6.32^1.1")
    with pytest.raises(Exception):   
        assert mat_module.evaluate("!")   
    with pytest.raises(Exception):   
        assert mat_module.evaluate("nieco")
    with pytest.raises(Exception):   
        assert mat_module.evaluate("0/0") 
    with pytest.raises(Exception):   
        assert mat_module.evaluate("log-5") 
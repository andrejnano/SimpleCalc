#!/bin/python

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

def test_sub():
    assert mat_module.sub(1.0,3.14159265358) == -2.14159265358 
    assert mat_module.sub(1,0) == 1
    assert mat_module.sub(42,-42) == 84
    assert mat_module.sub(-42,-42) == 0
    with pytest.raises(Exception):
        mat_module.sub(9.3333,"str")
    with pytest.raises(Exception):
        mat_module.sub("str","ing")
    with pytest.raises(Exception):
        mat_module.sub([1,-1.4142],[3,4])
    with pytest.raises(Exception):
        mat_module.factorial()
    with pytest.raises(Exception):
        mat_module.factorial(0,0,0)

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


def test_sqrt():
    assert mat_module.sqrt(6.022e+23) == 776015463763.4485 
    assert mat_module.sqrt(25) == 5
    assert mat_module.sqrt(0) == 0
    assert mat_module.sqrt(2) == 1.4142135623730951
    with pytest.raises(Exception):
        mat_module.sqrt(-2)
    with pytest.raises(Exception):
        mat_module.sqrt("str","ing")
    with pytest.raises(Exception):
        mat_module.sqrt([-0.451,2.77,3.4,64.4])
    with pytest.raises(Exception):
        mat_module.factorial()
    with pytest.raises(Exception):
        mat_module.factorial(-1.54,3)


def test_factorial():
    assert mat_module.factorial(5) == 120 
    assert mat_module.factorial(15) == 1307674368000
    assert mat_module.factorial(0) == 0
    assert mat_module.factorial(2) == 2
    with pytest.raises(Exception):
        mat_module.factorial(-2)
    with pytest.raises(Exception):
        mat_module.factorial("str","ing")
    with pytest.raises(Exception):
        mat_module.factorial(64.4)
    with pytest.raises(Exception):
        mat_module.factorial(1,2)
    with pytest.raises(Exception):
        mat_module.factorial()

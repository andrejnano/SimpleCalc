#!/bin/python

import random
import sys

a=int(sys.argv[1])
for i in range(a):
    r=random.uniform(-5,500)
    print("%.5f" % r)

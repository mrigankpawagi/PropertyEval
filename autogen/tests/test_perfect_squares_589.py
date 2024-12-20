import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
import math
import string
                
a = integers(min_value=0, max_value=MAX_INT)
b = integers(min_value=0, max_value=MAX_INT)

strategy = a, b
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def perfect_squares(a, b):
    lists=[]
    for i in range (a,b+1):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, perfect_squares, *args)

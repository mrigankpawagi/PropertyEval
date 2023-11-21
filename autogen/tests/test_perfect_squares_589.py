import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
a = integers(min_value=0, max_value=10000)
b = integers(min_value=0, max_value=10000)

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
def test_fuzz(args):
    run_with_timeout(0.3, perfect_squares, *args)

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
                
a = integers(min_value=1, max_value=MAX_INT)
b = integers(min_value=1, max_value=MAX_INT)

strategy = a, b
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sum(a,b): 
    sum = 0
    for i in range (1,min(a,b)): 
        if (a % i == 0 and b % i == 0): 
            sum += i 
    return sum

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, sum, *args)

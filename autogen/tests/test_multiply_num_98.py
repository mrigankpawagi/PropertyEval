import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
numbers = lists(floats(), min_size=1)

strategy = numbers
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def multiply_num(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total/len(numbers) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, multiply_num, *args)

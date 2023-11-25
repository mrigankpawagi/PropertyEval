import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
list1 = lists(integers(min_value=MIN_INT, max_value=-1), max_size=MAX_SEQUENCE_LEN)
strategy = list1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def largest_neg(list1): 
    max = list1[0] 
    for x in list1: 
        if x < max : 
             max = x  
    return max

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, largest_neg, *args)

import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
lst = lists(integers(min_value=MIN_INT, max_value=MAX_INT))

strategy = lst
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def Split(list): 
    od_li = [] 
    for i in list: 
        if (i % 2 != 0): 
            od_li.append(i)  
    return od_li

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, Split, *args)

import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
list1 = lists(lists(elements=integers()), min_size=1, max_size=MAX_SEQUENCE_LEN)
x = integers()

strategy = list1, x
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def count_element_in_list(list1, x): 
    ctr = 0
    for i in range(len(list1)): 
        if x in list1[i]: 
            ctr+= 1          
    return ctr

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, count_element_in_list, *args)

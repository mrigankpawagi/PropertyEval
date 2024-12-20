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
                
list1 = lists(lists(elements=[integers(), text()], min_size=1, max_size=MAX_SEQUENCE_LEN), min_size=1, max_size=MAX_SEQUENCE_LEN)
x = one_of(integers(), text())

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
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, count_element_in_list, *args)

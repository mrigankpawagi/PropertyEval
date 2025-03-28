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
                
list1 = lists(lists(integers()), max_size=MAX_SEQUENCE_LEN)

strategy = list1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def unique_sublists(list1):
    result ={}
    for l in  list1: 
        result.setdefault(tuple(l), list()).append(1) 
    for a, b in result.items(): 
        result[a] = sum(b)
    return result

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, unique_sublists, *args)

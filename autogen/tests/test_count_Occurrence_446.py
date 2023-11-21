import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
tup = lists(elements=one_of(integers(), characters()), min_size=1, max_size=MAX_SEQUENCE_LEN)
lst = lists(elements=one_of(integers(), characters()), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = tup, lst
if not isinstance(strategy, tuple):
    strategy = (strategy,)

from collections import Counter 
def count_Occurrence(tup, lst): 
    count = 0
    for item in tup: 
        if item in lst: 
            count+= 1 
    return count  

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, count_Occurrence, *args)

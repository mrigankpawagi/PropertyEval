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
                
tup = tuples(integers(), max_size=MAX_SEQUENCE_LEN)
lst = lists(integers(), max_size=MAX_SEQUENCE_LEN)

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
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, count_Occurrence, *args)

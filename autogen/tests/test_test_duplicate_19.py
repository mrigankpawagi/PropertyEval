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
                
arraynums = lists(integers(), max_size=MAX_SEQUENCE_LEN)
strategy = arraynums
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def test_duplicate(arraynums):
    nums_set = set(arraynums)    
    return len(arraynums) != len(nums_set)     

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, test_duplicate, *args)

import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
arraynums = lists(integers(min_value=MIN_INT, max_value=MAX_INT), unique=True, min_size=SMALL_SEQUENCE_LEN, max_size=MAX_SEQUENCE_LEN)

strategy = arraynums
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def test_duplicate(arraynums):
    nums_set = set(arraynums)    
    return len(arraynums) != len(nums_set)     

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, test_duplicate, *args)

import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
l = lists(integers(min_value=MIN_INT, max_value=MAX_INT), max_size=MAX_SEQUENCE_LEN)

strategy = l
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_Consecutive(l): 
    return sorted(l) == list(range(min(l),max(l)+1)) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, check_Consecutive, *args)

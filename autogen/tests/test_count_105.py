import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
lst = lists(elements=booleans(), max_size=MAX_SEQUENCE_LEN)

strategy = lst
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def count(lst):   
    return sum(lst) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, count, *args)

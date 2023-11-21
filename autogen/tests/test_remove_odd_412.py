import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
l = lists(integers(min_value=MIN_INT, max_value=MAX_INT), max_size=MAX_SEQUENCE_LEN)
evens = l.filter(lambda x: x % 2 == 0)

strategy = evens
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def remove_odd(l):
    for i in l:
        if i % 2 != 0:
            l.remove(i)
    return l

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, remove_odd, *args)
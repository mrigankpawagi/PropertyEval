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
                
l = lists(integers(), max_size=MAX_SEQUENCE_LEN)
strategy = l
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def remove_odd(l):
    for i in l:
        if i % 2 != 0:
            l.remove(i)
    return l

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, remove_odd, *args)

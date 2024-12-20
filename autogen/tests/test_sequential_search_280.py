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
                
dlist = lists(integers(), max_size=MAX_SEQUENCE_LEN)
item = integers()

strategy = dlist, item
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sequential_search(dlist, item):
    pos = 0
    found = False
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found, pos

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, sequential_search, *args)

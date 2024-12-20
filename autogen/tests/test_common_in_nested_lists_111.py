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
                
nestedlist = lists(lists(integers(), max_size=MAX_SEQUENCE_LEN), max_size=MAX_SEQUENCE_LEN)

strategy = nestedlist
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def common_in_nested_lists(nestedlist):
    result = list(set.intersection(*map(set, nestedlist)))
    return result

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, common_in_nested_lists, *args)

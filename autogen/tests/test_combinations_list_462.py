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
                
list1 = lists(elements=text(), min_size=0, max_size=MAX_SEQUENCE_LEN)
strategy = list1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def combinations_list(list1):
    if len(list1) == 0:
        return [[]]
    result = []
    for el in combinations_list(list1[1:]):
        result += [el, el+[list1[0]]]
    return result

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, combinations_list, *args)

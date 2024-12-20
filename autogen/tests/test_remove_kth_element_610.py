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
                
list1 = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)
L = integers(min_value=1, max_value=MAX_SEQUENCE_LEN)

strategy = list1, L
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def remove_kth_element(list1, L):
    return  list1[:L-1] + list1[L:]

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, remove_kth_element, *args)

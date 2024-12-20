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
                
list_data = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)
strategy = list_data
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def unique_product(list_data):
    temp = list(set(list_data))
    p = 1
    for i in temp:
        p *= i
    return p

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, unique_product, *args)

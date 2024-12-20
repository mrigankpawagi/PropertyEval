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
                
max_sum_list = lists(lists(integers()), max_size=MAX_SEQUENCE_LEN)
strategy = max_sum_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def max_sum_list(lists):
 return max(lists, key=sum)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, max_sum_list, *args)

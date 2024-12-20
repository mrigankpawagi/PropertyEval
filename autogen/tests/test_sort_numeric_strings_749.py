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
                
nums_str = lists(text(min_size=1, max_size=3, alphabet="0123456789"), max_size=MAX_SEQUENCE_LEN)
strategy = nums_str
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sort_numeric_strings(nums_str):
    result = [int(x) for x in nums_str]
    result.sort()
    return result

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, sort_numeric_strings, *args)

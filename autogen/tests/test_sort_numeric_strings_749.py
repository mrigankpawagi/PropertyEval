import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
nums_str = lists(text(alphabet="1234567890", min_size=1), max_size=MAX_SEQUENCE_LEN)

strategy = nums_str
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sort_numeric_strings(nums_str):
    result = [int(x) for x in nums_str]
    result.sort()
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, sort_numeric_strings, *args)

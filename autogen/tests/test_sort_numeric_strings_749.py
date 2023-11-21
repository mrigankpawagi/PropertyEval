import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
nums_str = lists(text(alphabet=digits(min_value=0, max_value=9), min_size=1, max_size=10), min_size=1, max_size=10)

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

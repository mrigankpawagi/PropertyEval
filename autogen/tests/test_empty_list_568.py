import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
strategy = integers(min_value=0, max_value=MAX_SEQUENCE_LEN)
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def empty_list(length):
 empty_list = [{} for _ in range(length)]
 return empty_list

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, empty_list, *args)

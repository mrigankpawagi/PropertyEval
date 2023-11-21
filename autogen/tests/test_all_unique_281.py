import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_list = lists(elements=integers(), unique=True, max_size=MAX_SEQUENCE_LEN)

strategy = test_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def all_unique(test_list):
    if len(test_list) > len(set(test_list)):
        return False
    return True

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, all_unique, *args)

import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_list = lists(integers(), max_size=MAX_SEQUENCE_LEN)
test_str = text(alphabet='abcdefghijklmnopqrstuvwxyz', max_size=MAX_SEQUENCE_LEN)

strategy = test_list, test_str
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def new_tuple(test_list, test_str):
  return tuple(test_list + [test_str])

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, new_tuple, *args)

import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_list = lists(lists(integers(), max_size=MAX_SEQUENCE_LEN), max_size=MAX_SEQUENCE_LEN)
N = integers(min_value=0, max_value=MAX_SEQUENCE_LEN-1)

strategy = test_list, N
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def max_of_nth(test_list, N):
  res = max([sub[N] for sub in test_list])
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, max_of_nth, *args)

import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_list = lists(tuples(integers(min_value=MIN_INT, max_value=MAX_INT), integers(min_value=MIN_INT, max_value=MAX_INT)), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = test_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def extract_freq(test_list):
  res = len(list(set(tuple(sorted(sub)) for sub in test_list)))
  return (res)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, extract_freq, *args)

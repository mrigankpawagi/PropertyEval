import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_tup = lists(integers(), min_size=2, max_size=MAX_SEQUENCE_LEN, unique=True)

strategy = test_tup
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def tuple_to_dict(test_tup):
  res = dict(test_tup[idx : idx + 2] for idx in range(0, len(test_tup), 2))
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, tuple_to_dict, *args)

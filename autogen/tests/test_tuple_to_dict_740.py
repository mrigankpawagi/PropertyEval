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
                
test_tup = lists(integers(), min_size=2, max_size=MAX_SEQUENCE_LEN, unique=True).map(tuple)
strategy = test_tup
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def tuple_to_dict(test_tup):
  res = dict(test_tup[idx : idx + 2] for idx in range(0, len(test_tup), 2))
  return (res) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, tuple_to_dict, *args)

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
                
test_list = lists(
    tuples(integers(), integers()),
    min_size=1,
    max_size=MAX_SEQUENCE_LEN
)

strategy = test_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def count_bidirectional(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return res

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, count_bidirectional, *args)

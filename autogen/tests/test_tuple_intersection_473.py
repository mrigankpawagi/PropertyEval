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
                
test_list1 = lists(tuples(integers(), integers()), max_size=MAX_SEQUENCE_LEN)
test_list2 = lists(tuples(integers(), integers()), max_size=MAX_SEQUENCE_LEN)

strategy = test_list1, test_list2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def tuple_intersection(test_list1, test_list2):
  res = set([tuple(sorted(ele)) for ele in test_list1]) & set([tuple(sorted(ele)) for ele in test_list2])
  return (res)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, tuple_intersection, *args)

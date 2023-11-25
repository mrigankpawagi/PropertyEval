import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_list1 = lists(integers(), max_size=MAX_SEQUENCE_LEN).map(tuple)
test_list2 = lists(integers(), max_size=MAX_SEQUENCE_LEN).map(tuple)

strategy = test_list1, test_list2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def tuple_intersection(test_list1, test_list2):
  res = set([tuple(sorted(ele)) for ele in test_list1]) & set([tuple(sorted(ele)) for ele in test_list2])
  return (res)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, tuple_intersection, *args)

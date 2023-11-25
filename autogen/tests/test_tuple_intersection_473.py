import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def find_intersection(draw):
    n = draw(integers(min_value=0, max_value=MAX_SEQUENCE_LEN))
    common_elements = draw(lists(integers(), min_size=n, max_size=n))
    list1 = draw(lists(integers(), min_size=n, max_size=n))
    list2 = draw(lists(integers(), min_size=n, max_size=n))
    
    test_list1 = draw(lists(sampled_from(list1), min_size=n, max_size=n))
    test_list2 = draw(lists(sampled_from(list2), min_size=n, max_size=n))
    
    return common_elements, test_list1, test_list2

strategy = find_intersection()
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def tuple_intersection(test_list1, test_list2):
  res = set([tuple(sorted(ele)) for ele in test_list1]) & set([tuple(sorted(ele)) for ele in test_list2])
  return (res)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, tuple_intersection, *args)

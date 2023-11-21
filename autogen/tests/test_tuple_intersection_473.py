import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_tuple_list(draw):
    n = draw(integers(min_value=1, max_value=10))
    tuple_list = draw(lists(tuples(integers(), integers()), min_size=n, max_size=n))
    return tuple_list

tuple_list1 = create_tuple_list()
tuple_list2 = create_tuple_list()

strategy = tuple_list1, tuple_list2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def tuple_intersection(test_list1, test_list2):
  res = set([tuple(sorted(ele)) for ele in test_list1]) & set([tuple(sorted(ele)) for ele in test_list2])
  return (res)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, tuple_intersection, *args)

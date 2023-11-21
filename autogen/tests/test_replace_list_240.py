import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
list1 = lists(integers(), min_size=0)
list2 = lists(integers(), min_size=0)

strategy = list1, list2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def replace_list(list1,list2):
 list1[-1:] = list2
 replace_list=list1
 return replace_list


@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, replace_list, *args)

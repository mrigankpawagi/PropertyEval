import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
list1 = lists(lists(text(), min_size=1))

strategy = list1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sort_sublists(list1):
    result = list(map(sorted,list1)) 
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, sort_sublists, *args)

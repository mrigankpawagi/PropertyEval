import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
list1 = lists(dictionaries(keys=text(), values=any_type()), min_size=0)

strategy = list1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def empty_dit(list1):
 empty_dit=all(not d for d in list1)
 return empty_dit

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, empty_dit, *args)
import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
list1 = lists(elements=integers(), max_size=MAX_SEQUENCE_LEN)
list2 = lists(elements=integers(), max_size=MAX_SEQUENCE_LEN)

strategy = list1, list2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def remove_elements(list1, list2):
    result = [x for x in list1 if x not in list2]
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, remove_elements, *args)

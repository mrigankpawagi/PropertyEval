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
                
list1 = lists(integers(), max_size=MAX_SEQUENCE_LEN)
list2 = lists(integers(), max_size=MAX_SEQUENCE_LEN)

strategy = list1, list2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def remove_elements(list1, list2):
    result = [x for x in list1 if x not in list2]
    return result

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, remove_elements, *args)

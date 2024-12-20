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
                
list1 = lists(lists(text(), min_size=1, max_size=MAX_SEQUENCE_LEN), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = list1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sort_sublists(list1):
    result = list(map(sorted,list1)) 
    return result

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, sort_sublists, *args)

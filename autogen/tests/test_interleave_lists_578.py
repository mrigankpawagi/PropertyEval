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
                
list_len = integers(min_value=1, max_value=5)  # Assuming the maximum length of the input lists is 5
list_ele = integers(min_value=0, max_value=100)  # Assuming the elements of the lists can be any integer from 0 to 100

list1 = lists(list_ele, min_size=1, max_size=list_len)
list2 = lists(list_ele, min_size=1, max_size=list_len)
list3 = lists(list_ele, min_size=1, max_size=list_len)

strategy = list1, list2, list3
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def interleave_lists(list1,list2,list3):
    result = [el for pair in zip(list1, list2, list3) for el in pair]
    return result

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, interleave_lists, *args)

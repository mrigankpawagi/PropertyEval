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
                
list1 = lists(integers())
strategy = list1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def issort_list(list1):
    result = all(list1[i] <= list1[i+1] for i in range(len(list1)-1))
    return result

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, issort_list, *args)

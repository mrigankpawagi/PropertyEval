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

def common_element(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, common_element, *args)

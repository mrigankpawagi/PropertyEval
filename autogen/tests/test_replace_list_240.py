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
                
list1 = lists(integers() | characters(), min_size=1, max_size=MAX_SEQUENCE_LEN)
list2 = lists(integers() | characters(), min_size=0, max_size=MAX_SEQUENCE_LEN)

strategy = list1, list2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def replace_list(list1,list2):
 list1[-1:] = list2
 replace_list=list1
 return replace_list


@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, replace_list, *args)

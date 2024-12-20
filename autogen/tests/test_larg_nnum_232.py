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
n = integers(min_value=1, max_value=MAX_SEQUENCE_LEN)

strategy = list1, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import heapq
def larg_nnum(list1,n):
 largest=heapq.nlargest(n,list1)
 return largest

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, larg_nnum, *args)

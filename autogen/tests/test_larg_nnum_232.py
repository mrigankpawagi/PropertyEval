import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
list1 = lists(integers(min_value=MIN_INT, max_value=MAX_INT), min_size=1, max_size=MAX_SEQUENCE_LEN)
n = integers(min_value=1, max_value=MAX_SEQUENCE_LEN)

strategy = list1, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import heapq
def larg_nnum(list1,n):
 largest=heapq.nlargest(n,list1)
 return largest

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, larg_nnum, *args)

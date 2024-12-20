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
                
n = integers(min_value=0, max_value=sys.maxsize)

strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def count_Set_Bits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, count_Set_Bits, *args)

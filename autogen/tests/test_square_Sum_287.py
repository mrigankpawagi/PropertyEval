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
                
n = integers(min_value=0, max_value=MAX_SEQUENCE_LEN)
strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def square_Sum(n):  
    return int(2*n*(n+1)*(2*n+1)/3)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, square_Sum, *args)

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
                
a = integers(min_value=MIN_INT, max_value=MAX_INT)
b = integers(min_value=MIN_INT, max_value=MAX_INT)

strategy = a, b
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def is_Power_Of_Two (x): 
    return x and (not(x & (x - 1))) 
def differ_At_One_Bit_Pos(a,b): 
    return is_Power_Of_Two(a ^ b)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, differ_At_One_Bit_Pos, *args)

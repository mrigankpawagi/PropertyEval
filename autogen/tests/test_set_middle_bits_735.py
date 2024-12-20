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
                
n = integers(min_value=0, max_value=2**31 - 1)

strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def set_middle_bits(n):  
    n |= n >> 1; 
    n |= n >> 2; 
    n |= n >> 4; 
    n |= n >> 8; 
    n |= n >> 16;  
    return (n >> 1) ^ 1
def toggle_middle_bits(n): 
    if (n == 1): 
        return 1
    return n ^ set_middle_bits(n) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, set_middle_bits, *args)

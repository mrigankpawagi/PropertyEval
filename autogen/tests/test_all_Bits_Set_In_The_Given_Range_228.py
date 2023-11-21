import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=0, max_value=MAX_INT)
l = integers(min_value=0, max_value=MAX_INT)
r = integers(min_value=0, max_value=MAX_INT)

strategy = n, l, r
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def all_Bits_Set_In_The_Given_Range(n,l,r):  
    num = (((1 << r) - 1) ^ ((1 << (l - 1)) - 1)) 
    new_num = n & num
    if (new_num == 0): 
        return True
    return False

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, all_Bits_Set_In_The_Given_Range, *args)

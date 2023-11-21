import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from hypothesis import strategies as st

n = st.integers(min_value=0)
l = st.integers(min_value=1)
r = st.integers(min_value=1)

strategy = st.tuples(n, l, r)
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

import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def power_of_two(draw):
    n = draw(integers(min_value=0, max_value=30))
    return 2 ** n

x = power_of_two()

strategy = x
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def is_Power_Of_Two (x): 
    return x and (not(x & (x - 1))) 
def differ_At_One_Bit_Pos(a,b): 
    return is_Power_Of_Two(a ^ b)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, is_Power_Of_Two, *args)

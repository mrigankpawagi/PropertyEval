import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from hypothesis import strategies as st

a = st.integers(min_value=0)
b = st.integers(min_value=0)

strategy = st.tuples(a, b)
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sum(a,b): 
    sum = 0
    for i in range (1,min(a,b)): 
        if (a % i == 0 and b % i == 0): 
            sum += i 
    return sum

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, sum, *args)

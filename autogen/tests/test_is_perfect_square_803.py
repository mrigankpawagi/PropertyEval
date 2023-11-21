import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=0)

strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def is_perfect_square(n) :
    i = 1
    while (i * i<= n):
        if ((n % i == 0) and (n / i == i)):
            return True     
        i = i + 1
    return False

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, is_perfect_square, *args)

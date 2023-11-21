import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
number = integers(min_value=MIN_INT, max_value=MAX_INT)

strategy = number
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sum_div(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, sum_div, *args)

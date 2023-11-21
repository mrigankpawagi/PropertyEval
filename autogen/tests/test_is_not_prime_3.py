import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=2, max_value=10**5)

strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math
def is_not_prime(n):
    result = False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            result = True
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, is_not_prime, *args)

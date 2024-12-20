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
                
n = integers(min_value=0)
strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def count_Primes_nums(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, count_Primes_nums, *args)

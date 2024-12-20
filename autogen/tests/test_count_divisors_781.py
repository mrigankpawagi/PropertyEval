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
                
n = integers(min_value=1, max_value=1000)
strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math 
def count_divisors(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 2 == 0

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, count_divisors, *args)

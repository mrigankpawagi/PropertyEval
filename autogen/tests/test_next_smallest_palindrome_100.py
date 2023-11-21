import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
num = integers(min_value=0, max_value=10000)

strategy = num
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import sys
def next_smallest_palindrome(num):
    numstr = str(num)
    for i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, next_smallest_palindrome, *args)

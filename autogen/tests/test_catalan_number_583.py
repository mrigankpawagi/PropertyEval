import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
num = integers(min_value=0, max_value=10)
strategy = num
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def catalan_number(num):
    if num <=1:
         return 1   
    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num-i-1)
    return res_num

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, catalan_number, *args)

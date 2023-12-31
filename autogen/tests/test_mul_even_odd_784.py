import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
list1 = lists(integers(), min_size=2, max_size=MAX_SEQUENCE_LEN).filter(lambda x: len(x) >= 2)

strategy = list1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def mul_even_odd(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even*first_odd)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, mul_even_odd, *args)

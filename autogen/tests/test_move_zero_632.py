import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
num_list = lists(integers(), max_size=MAX_SEQUENCE_LEN)

strategy = num_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def move_zero(num_list):
    a = [0 for i in range(num_list.count(0))]
    x = [i for i in num_list if i != 0]
    return x + a

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, move_zero, *args)

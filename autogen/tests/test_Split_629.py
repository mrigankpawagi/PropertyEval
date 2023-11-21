import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_list(draw):
    n = draw(integers(min_value=0, max_value=10))
    lst = draw(lists(integers(min_value=0, max_value=10), min_size=n, max_size=n))
    return lst

lst = create_list()

strategy = lst
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def Split(list): 
    return [num for num in list if num % 2 == 0]

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, Split, *args)

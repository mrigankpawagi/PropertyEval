import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from hypothesis import strategies as st

list_data = st.lists(st.integers(), min_size=0, unique=True)

strategy = list_data
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def unique_product(list_data):
    temp = list(set(list_data))
    p = 1
    for i in temp:
        p *= i
    return p

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, unique_product, *args)
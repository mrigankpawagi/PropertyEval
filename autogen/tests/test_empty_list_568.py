import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from hypothesis import strategies as st

length = st.integers(min_value=0, max_value=100)

strategy = length
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def empty_list(length):
 empty_list = [{} for _ in range(length)]
 return empty_list

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, empty_list, *args)

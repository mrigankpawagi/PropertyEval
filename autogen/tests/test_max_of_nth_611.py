import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_matrix(draw):
    n = draw(integers(min_value=1, max_value=10))
    matrix = draw(lists(lists(integers(), min_size=n, max_size=n), min_size=n, max_size=n))
    return matrix

@composite
def create_positive_integer(draw):
    n = draw(integers(min_value=1, max_value=10))
    return n

test_list = create_matrix()
N = create_positive_integer()

strategy = test_list, N
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def max_of_nth(test_list, N):
  res = max([sub[N] for sub in test_list])
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, max_of_nth, *args)

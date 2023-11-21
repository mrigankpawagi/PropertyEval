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
    m = draw(integers(min_value=1, max_value=10))
    matrix = draw(lists(lists(integers(), min_size=m, max_size=m), min_size=n, max_size=n))
    return matrix

M = create_matrix()

strategy = M
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sort_matrix(M):
    result = sorted(M, key=sum)
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, sort_matrix, *args)

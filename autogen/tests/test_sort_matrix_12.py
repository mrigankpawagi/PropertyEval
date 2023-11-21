import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from typing import List
from hypothesis import strategies as st

def sort_matrix(M: List[List[int]]) -> List[List[int]]:
    return sorted(M, key=lambda row: sum(row))

matrix_strategy = st.lists(st.lists(st.integers()))

strategy = matrix_strategy,
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sort_matrix(M):
    result = sorted(M, key=sum)
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, sort_matrix, *args)

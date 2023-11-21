import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from typing import List

from hypothesis import strategies as st, given


def magic_square_test(matrix: List[List[int]]) -> bool:
    """
    Calculate whether the matrix is a magic square.

    Args:
        matrix: The matrix to check.

    Returns:
        True if the matrix is a magic square, False otherwise.
    """
    n = len(matrix)
    target_sum = sum(matrix[0])

    # Check rows
    if any(sum(row) != target_sum for row in matrix):
        return False

    # Check columns
    if any(sum(col) != target_sum for col in zip(*matrix)):
        return False

    # Check diagonals
    if sum(matrix[i][i] for i in range(n)) != target_sum:
        return False
    if sum(matrix[i][n - i - 1] for i in range(n)) != target_sum:
        return False

    return True


@given(st.lists(st.lists(st.integers())))
def test_magic_square(matrix):
    magic_square_test(matrix)


test_magic_square()
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def magic_square_test(my_matrix):
    iSize = len(my_matrix[0])
    sum_list = []
    sum_list.extend([sum (lines) for lines in my_matrix])   
    for col in range(iSize):
        sum_list.append(sum(row[col] for row in my_matrix))
    result1 = 0
    for i in range(0,iSize):
        result1 +=my_matrix[i][i]
    sum_list.append(result1)      
    result2 = 0
    for i in range(iSize-1,-1,-1):
        result2 +=my_matrix[i][i]
    sum_list.append(result2)
    if len(set(sum_list))>1:
        return False
    return True

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, magic_square_test, *args)

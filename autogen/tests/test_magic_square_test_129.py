import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
import math
import string
                
my_matrix = lists(lists(integers(min_value=0, max_value=100), min_size=3, max_size=3), min_size=3, max_size=3)

strategy = my_matrix
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
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, magic_square_test, *args)

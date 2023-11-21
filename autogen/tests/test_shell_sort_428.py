import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
my_list = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = my_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def shell_sort(my_list):
    gap = len(my_list) // 2
    while gap > 0:
        for i in range(gap, len(my_list)):
            current_item = my_list[i]
            j = i
            while j >= gap and my_list[j - gap] > current_item:
                my_list[j] = my_list[j - gap]
                j -= gap
            my_list[j] = current_item
        gap //= 2

    return my_list

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, shell_sort, *args)

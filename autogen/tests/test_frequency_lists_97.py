import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
def frequency_list():
    elements = lists(integers(), min_size=1, max_size=10)
    return elements

list1 = frequency_list()
strategy = list1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def frequency_lists(list1):
    list1 = [item for sublist in list1 for item in sublist]
    dic_data = {}
    for num in list1:
        if num in dic_data.keys():
            dic_data[num] += 1
        else:
            key = num
            value = 1
            dic_data[key] = value
    return dic_data


@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, frequency_lists, *args)

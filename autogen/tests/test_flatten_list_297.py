import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
def create_nested_list():
    base = integers()
    return recursive(base, lists)

list1 = create_nested_list()
strategy = list1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def flatten_list(list1):
    result_list = []
    if not list1: return result_list
    stack = [list(list1)]
    while stack:
        c_num = stack.pop()
        next = c_num.pop()
        if c_num: stack.append(c_num)
        if isinstance(next, list):
            if next: stack.append(list(next))
        else: result_list.append(next)
    result_list.reverse()
    return result_list 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, flatten_list, *args)

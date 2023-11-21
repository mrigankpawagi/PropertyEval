import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from hypothesis.strategies import integers, text, tuples

def tuple_str_int(test_str):
    int_list = [int(x) for x in test_str.strip('()').split(', ')]
    return tuple(int_list)

test_str = text().map(lambda x: f'({x})')

strategy = test_str.map(tuple_str_int)
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def tuple_str_int(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('...', '').split(', '))
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, tuple_str_int, *args)

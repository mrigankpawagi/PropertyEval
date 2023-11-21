import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
import ast

def remove_paren(test_str):
    test_str = test_str.replace('(', '').replace(')', '')
    return test_str

strategy = text(min_size=1).filter(lambda x: '(' in x and ')' in x).map(remove_paren).map(lambda x: ast.literal_eval(x))
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def tuple_str_int(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('...', '').split(', '))
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, tuple_str_int, *args)

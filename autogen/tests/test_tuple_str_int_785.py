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
                
test_str = from_regex(r"\(\d+(,\s*\d+)*\)")
strategy = test_str.map(tuple_str_int)
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def tuple_str_int(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('...', '').split(', '))
  return (res) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, tuple_str_int, *args)

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
                
test_list = lists(text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=5), max_size=2)
test_str = text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=5)

strategy = test_list, test_str
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def new_tuple(test_list, test_str):
  return tuple(test_list + [test_str])

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, new_tuple, *args)

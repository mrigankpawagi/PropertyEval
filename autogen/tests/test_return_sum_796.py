import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
keys = lists(text(alphabet=string.ascii_lowercase, min_size=1, max_size=1), unique=True, min_size=1, max_size=5)
values = lists(integers(min_value=0, max_value=100), min_size=1, max_size=5)

strategy = dictionaries(keys, values)
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def return_sum(dict):
  sum = 0
  for i in dict.values():
    sum = sum + i
  return sum

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, return_sum, *args)

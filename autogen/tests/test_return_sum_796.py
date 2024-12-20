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
                
dict = dictionaries(text(), integers(), max_size=MAX_SEQUENCE_LEN)
strategy = dict
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def return_sum(dict):
  sum = 0
  for i in dict.values():
    sum = sum + i
  return sum

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, return_sum, *args)

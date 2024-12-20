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
                
list1 = lists(floats(), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = list1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def round_and_sum(list1):
  lenght=len(list1)
  round_and_sum=sum(list(map(round,list1))* lenght)
  return round_and_sum

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, round_and_sum, *args)

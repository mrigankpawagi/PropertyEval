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
                
lst1 = lists(integers(), max_size=MAX_SEQUENCE_LEN)
lst2 = lists(integers(), max_size=MAX_SEQUENCE_LEN)

strategy = lst1, lst2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sum_list(lst1,lst2):
  res_list = [lst1[i] + lst2[i] for i in range(len(lst1))] 
  return res_list

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, sum_list, *args)

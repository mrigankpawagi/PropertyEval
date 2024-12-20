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
                
test_list = lists(lists(text(alphabet="ab") | integers().map(str) | floats().map(str), max_size=MAX_SEQUENCE_LEN).map(tuple), max_size=MAX_SEQUENCE_LEN)

strategy = test_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def list_to_float(test_list):
  res = []
  for tup in test_list:
    temp = []
    for ele in tup:
      if ele.isalpha():
        temp.append(ele)
      else:
        temp.append(float(ele))
    res.append((temp[0],temp[1])) 
  return res

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, list_to_float, *args)

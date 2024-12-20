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
                
inner = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)
test_list = lists(inner, min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = test_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def extract_singly(test_list):
  res = []
  temp = set()
  for inner in test_list:
    for ele in inner:
      if not ele in temp:
        temp.add(ele)
        res.append(ele)
  return (res) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, extract_singly, *args)

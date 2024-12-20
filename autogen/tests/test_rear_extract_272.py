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
                
test_list = lists(tuples(integers(), text()), max_size=MAX_SEQUENCE_LEN).filter(lambda x: len(x) > 0)
strategy = test_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def rear_extract(test_list):
  res = [lis[-1] for lis in test_list]
  return (res) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, rear_extract, *args)

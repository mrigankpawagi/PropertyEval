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
                
test_tup1 = tuples(*([integers()] * 4))
test_tup2 = tuples(*([integers()] * 4))

strategy = test_tup1, test_tup2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def division_elements(test_tup1, test_tup2):
  res = tuple(ele1 // ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
  return (res) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, division_elements, *args)

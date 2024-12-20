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
                
test_tuple = tuples(text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=10))
strategy = test_tuple
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def extract_rear(test_tuple):
  res = list(sub[len(sub) - 1] for sub in test_tuple)
  return (res) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, extract_rear, *args)

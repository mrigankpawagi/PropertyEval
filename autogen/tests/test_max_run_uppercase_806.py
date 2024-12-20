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
                
test_str = text(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', max_size=MAX_SEQUENCE_LEN).filter(str.isupper)
strategy = test_str
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def max_run_uppercase(test_str):
  cnt = 0
  res = 0
  for idx in range(0, len(test_str)):
    if test_str[idx].isupper():
      cnt += 1
    else:
      res = cnt
      cnt = 0
  if test_str[len(test_str) - 1].isupper():
    res = cnt
  return (res)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, max_run_uppercase, *args)

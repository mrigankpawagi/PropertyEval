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
                
s = text(alphabet='abcdefghijklmnopqrstuvwxyz', max_size=MAX_SEQUENCE_LEN)
strategy = s
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def count_occurance(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] == 's' and s[i+1] == 't' and s[i+2] == 'd'):
      count = count + 1
  return count

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, count_occurance, *args)

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
                
from hypothesis.strategies import text

s = text(alphabet="abcdef", max_size=MAX_SEQUENCE_LEN).filter(lambda x: x == "" or x.islower())

strategy = s
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, odd_values_string, *args)

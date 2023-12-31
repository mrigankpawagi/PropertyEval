import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
import string
string_inp = text(alphabet=string.ascii_lowercase, min_size=0, max_size=MAX_SEQUENCE_LEN).filter(lambda x: len(x) % 2 == 0)
strategy = string_inp
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, odd_values_string, *args)

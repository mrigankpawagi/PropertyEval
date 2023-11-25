import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_str = text(alphabet='abcdefghijklmnopqrstuvwxyz0123456789', max_size=MAX_SEQUENCE_LEN)
strategy = test_str
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def move_num(test_str):
  res = ''
  dig = ''
  for ele in test_str:
    if ele.isdigit():
      dig += ele
    else:
      res += ele
  res += dig
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, move_num, *args)

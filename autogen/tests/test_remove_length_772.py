import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_str = text(alphabet=characters(), min_size=1)
K = integers(min_value=0)

strategy = test_str, K
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def remove_length(test_str, K):
  temp = test_str.split()
  res = [ele for ele in temp if len(ele) != K]
  res = ' '.join(res)
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, remove_length, *args)

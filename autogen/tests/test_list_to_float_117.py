import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def make_list(draw):
    inner_list = lists(numbers(), min_size=1, max_size=10).map(lambda x: [str(n) for n in x])
    return draw(inner_list)

test_list = make_list()
strategy = test_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def list_to_float(test_list):
  res = []
  for tup in test_list:
    temp = []
    for ele in tup:
      if ele.isalpha():
        temp.append(ele)
      else:
        temp.append(float(ele))
    res.append((temp[0],temp[1])) 
  return res

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, list_to_float, *args)

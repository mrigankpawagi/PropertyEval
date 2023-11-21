import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_list = lists(tuples(text(), integers()))

strategy = test_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

from operator import itemgetter 
def index_minimum(test_list):
  res = min(test_list, key = itemgetter(1))[0]
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, index_minimum, *args)

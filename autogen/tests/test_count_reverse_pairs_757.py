import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_list = lists(text(), max_size=MAX_SEQUENCE_LEN)
strategy = test_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def count_reverse_pairs(test_list):
  res = sum([1 for idx in range(0, len(test_list)) for idxn in range(idx, len( 
	test_list)) if test_list[idxn] == str(''.join(list(reversed(test_list[idx]))))]) 
  return res

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, count_reverse_pairs, *args)

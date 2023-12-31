import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
list1 = lists(booleans() | floats() | integers() | text(max_size=MAX_SEQUENCE_LEN))
strategy = list1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import collections
def freq_count(list1):
  freq_count= collections.Counter(list1)
  return freq_count

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, freq_count, *args)

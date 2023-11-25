import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
k = one_of(characters(), integers(min_value=0, max_value=127))
strategy = k
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def ascii_value(k):
  ch=k
  return ord(ch)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, ascii_value, *args)

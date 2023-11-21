import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
tup1 = tuples(elements=characters(), min_size=1)

strategy = tup1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def tup_string(tup1):
  str =  ''.join(tup1)
  return str

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, tup_string, *args)

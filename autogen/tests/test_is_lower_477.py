import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
string = text(alphabet=string.ascii_letters, min_size=1)

strategy = string
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def is_lower(string):
  return (string.lower())

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, is_lower, *args)

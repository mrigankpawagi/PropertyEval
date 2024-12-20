import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
import math
import string
                
string = text(alphabet=string.ascii_letters, max_size=MAX_SEQUENCE_LEN).filter(lambda x: x.islower())
strategy = string
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def is_lower(string):
  return (string.lower())

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, is_lower, *args)

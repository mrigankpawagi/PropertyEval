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
                
string = text(alphabet='abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ', min_size=1, max_size=MAX_SEQUENCE_LEN)
strategy = string
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def replace_spaces(string):
  return string.replace(" ", "%20")

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, replace_spaces, *args)

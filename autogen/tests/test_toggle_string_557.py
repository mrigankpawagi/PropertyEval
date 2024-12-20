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
                
string = text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', min_size=1, max_size=MAX_SEQUENCE_LEN)
strategy = string
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def toggle_string(string):
 string1 = string.swapcase()
 return string1

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, toggle_string, *args)

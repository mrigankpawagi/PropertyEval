import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
string = text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', max_size=MAX_SEQUENCE_LEN)
strategy = string
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def toggle_string(string):
 string1 = string.swapcase()
 return string1

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, toggle_string, *args)

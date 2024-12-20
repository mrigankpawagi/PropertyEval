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
                
str1 = text(alphabet='abcdefghijklmnopqrstuvwxyz0123456789', min_size=1, max_size=MAX_SEQUENCE_LEN)
strategy = str1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def string_to_tuple(str1):
    result = tuple(x for x in str1 if not x.isspace()) 
    return result

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, string_to_tuple, *args)

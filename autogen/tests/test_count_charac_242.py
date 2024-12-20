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
                
str1 = text(max_size=MAX_SEQUENCE_LEN)
strategy = str1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def count_charac(str1):
 total = 0
 for i in str1:
    total = total + 1
 return total

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, count_charac, *args)

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
                
stringlist = lists(text(), min_size=1, max_size=MAX_SEQUENCE_LEN)
strategy = stringlist
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def reverse_string_list(stringlist):
    result = [x[::-1] for x in stringlist]
    return result

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, reverse_string_list, *args)

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
                
list1 = lists(text(alphabet=characters(min_codepoint=97, max_codepoint=122)), min_size=1, max_size=MAX_SEQUENCE_LEN)
strategy = list1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def len_log(list1):
    max=len(list1[0])
    for i in list1:
        if len(i)>max:
            max=len(i)
    return max

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, len_log, *args)

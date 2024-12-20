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
                
str_list = lists(text(), min_size=1, max_size=MAX_SEQUENCE_LEN)
l = integers(min_value=1)

strategy = str_list, l
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def extract_string(str, l):
    result = [e for e in str if len(e) == l] 
    return result

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, extract_string, *args)

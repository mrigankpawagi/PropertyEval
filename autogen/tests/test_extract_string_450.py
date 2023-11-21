import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
str_list = lists(text(), min_size=1, max_size=MAX_SEQUENCE_LEN)
l = integers(min_value=1, max_value=MAX_SEQUENCE_LEN)

strategy = str_list, l
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def extract_string(str, l):
    result = [e for e in str if len(e) == l] 
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, extract_string, *args)

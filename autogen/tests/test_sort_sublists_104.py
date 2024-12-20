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
                
input_list = lists(lists(text(alphabet=string.ascii_letters, min_size=1)), max_size=MAX_SEQUENCE_LEN)

strategy = input_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sort_sublists(input_list):
    result = [sorted(x, key = lambda x:x[0]) for x in input_list] 
    return result


@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, sort_sublists, *args)

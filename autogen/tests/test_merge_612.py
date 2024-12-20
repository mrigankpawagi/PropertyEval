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
                
lst = lists(lists(elements=tuple(elements(text(), text())), min_size=1, max_size=MAX_SEQUENCE_LEN), min_size=1, max_size=MAX_SEQUENCE_LEN).map(lambda lst: [list(x) for x in zip(*lst)])

strategy = lst
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def merge(lst):  
    return [list(ele) for ele in list(zip(*lst))] 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, merge, *args)

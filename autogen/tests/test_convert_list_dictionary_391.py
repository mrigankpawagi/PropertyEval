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
                
l1 = lists(text(alphabet='abcd', min_size=2, max_size=4))
l2 = lists(text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', min_size=2, max_size=10))
l3 = lists(integers(min_value=0, max_value=100))

strategy = l1, l2, l3
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def convert_list_dictionary(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return result

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, convert_list_dictionary, *args)

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
                
string = text()
strategy = string.map(lambda s: [s])
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def string_to_list(string): 
    lst = list(string.split(" ")) 
    return lst

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, string_to_list, *args)

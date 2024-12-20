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
                
str_len = integers(min_value=1, max_value=10)
strategy = str_len.map(lambda x: "a" * x)
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def number_of_substrings(str): 
	str_len = len(str); 
	return int(str_len * (str_len + 1) / 2); 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, number_of_substrings, *args)

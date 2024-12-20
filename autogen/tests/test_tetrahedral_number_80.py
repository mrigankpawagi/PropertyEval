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
                
n = integers(min_value=0, max_value=10**6)
strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def tetrahedral_number(n): 
	return (n * (n + 1) * (n + 2)) / 6

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, tetrahedral_number, *args)

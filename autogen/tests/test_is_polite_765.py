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
                
n = integers(min_value=1, max_value=10)

strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math 
def is_polite(n): 
	n = n + 1
	return (int)(n+(math.log((n + math.log(n, 2)), 2))) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, is_polite, *args)

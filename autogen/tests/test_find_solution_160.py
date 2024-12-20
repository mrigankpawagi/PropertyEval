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
                
a = integers(min_value=1, max_value=MAX_INT)
b = integers(min_value=1, max_value=MAX_INT)
n = integers(min_value=0, max_value=MAX_INT)

strategy = a, b, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_solution(a, b, n):
	i = 0
	while i * a <= n:
		if (n - (i * a)) % b == 0: 
			return (i, (n - (i * a)) // b)
		i = i + 1
	return None

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, find_solution, *args)

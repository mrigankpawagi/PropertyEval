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
                
n = integers(min_value=0, max_value=100)
strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def get_max_sum (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, get_max_sum, *args)

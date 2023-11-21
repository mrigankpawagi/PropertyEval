import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
a = integers(min_value=MIN_INT, max_value=MAX_INT)
b = integers(min_value=MIN_INT, max_value=MAX_INT)

strategy = a, b
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def power(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-1)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, power, *args)

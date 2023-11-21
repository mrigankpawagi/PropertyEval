import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
x = integers(min_value=0)

strategy = x
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def is_woodall(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 == 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return False

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, is_woodall, *args)

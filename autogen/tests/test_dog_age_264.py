import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
h_age = integers(min_value=1)

strategy = h_age
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def dog_age(h_age):
 if h_age < 0:
 	exit()
 elif h_age <= 2:
	 d_age = h_age * 10.5
 else:
	 d_age = 21 + (h_age - 2)*4
 return d_age

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, dog_age, *args)

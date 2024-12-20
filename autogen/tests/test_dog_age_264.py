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
                
h_age = integers(min_value=0, max_value=24)
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
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, dog_age, *args)

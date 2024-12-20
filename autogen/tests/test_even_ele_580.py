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
                
test_tuple = recursive((integers() | tuples()), max_leaves=MAX_SEQUENCE_LEN)
strategy = test_tuple
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def even_ele(test_tuple, even_fnc): 
	res = tuple() 
	for ele in test_tuple: 
		if isinstance(ele, tuple): 
			res += (even_ele(ele, even_fnc), ) 
		elif even_fnc(ele): 
			res += (ele, ) 
	return res 
def extract_even(test_tuple):
  res = even_ele(test_tuple, lambda x: x % 2 == 0)
  return (res) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, even_ele, *args)

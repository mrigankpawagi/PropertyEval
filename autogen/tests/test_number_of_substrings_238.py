import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
string = text(alphabet='abcdefghijklmnopqrstuvwxyz')

strategy = string
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def number_of_substrings(str): 
	str_len = len(str); 
	return int(str_len * (str_len + 1) / 2); 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, number_of_substrings, *args)

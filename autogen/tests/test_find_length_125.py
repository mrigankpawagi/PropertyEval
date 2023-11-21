import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
string = text(alphabet='01', min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = string
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_length(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_length, *args)

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
                
strs = text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', max_size=MAX_SEQUENCE_LEN).filter(lambda x: x == "" or x.islower())
strategy = strs
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def lps(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, lps, *args)

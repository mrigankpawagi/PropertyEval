import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
m = integers(min_value=1, max_value=10)
n = integers(min_value=1, max_value=10)

strategy = m, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def get_total_number_of_sequences(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, get_total_number_of_sequences, *args)

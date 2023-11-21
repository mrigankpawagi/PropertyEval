import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_strings(draw):
    n = draw(integers(min_value=1, max_value=10))
    strings = draw(lists(text(min_size=n, max_size=n), min_size=3, max_size=3))
    return strings

X, Y, Z = create_strings()

strategy = X, Y, Z
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def lcs_of_three(X, Y, Z): 
  m = len(X)
  n = len(Y)
  o = len(Z)
  L = [[[0 for i in range(o+1)] for j in range(n+1)] for k in range(m+1)]
  for i in range(m+1): 
	  for j in range(n+1): 
		  for k in range(o+1): 
			  if (i == 0 or j == 0 or k == 0): 
				  L[i][j][k] = 0
			  elif (X[i-1] == Y[j-1] and X[i-1] == Z[k-1]): 
				  L[i][j][k] = L[i-1][j-1][k-1] + 1
			  else: 
				  L[i][j][k] = max(max(L[i-1][j][k], L[i][j-1][k]), L[i][j][k-1]) 
  return L[m][n][o]

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, lcs_of_three, *args)

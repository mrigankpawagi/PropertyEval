import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
                
X = text(alphabet='abcdef', max_size=MAX_SEQUENCE_LEN)
Y = text(alphabet='abcdef', max_size=MAX_SEQUENCE_LEN)
Z = text(alphabet='abcdef', max_size=MAX_SEQUENCE_LEN)

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
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, lcs_of_three, *args)

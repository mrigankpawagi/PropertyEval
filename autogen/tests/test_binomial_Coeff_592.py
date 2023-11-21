import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=0, max_value=100)
k = integers(min_value=0, max_value=100)

strategy = n, k
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def binomial_Coeff(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def sum_Of_product(n): 
    return binomial_Coeff(2 * n,n - 1); 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, binomial_Coeff, *args)

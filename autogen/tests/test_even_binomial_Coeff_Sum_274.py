import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=1, max_value=MAX_INT)
strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math  
def even_binomial_Coeff_Sum( n): 
    return (1 << (n - 1)) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, even_binomial_Coeff_Sum, *args)

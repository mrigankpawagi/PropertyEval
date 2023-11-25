import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
strr = text(alphabet=string.ascii_letters, min_size=1, max_size=MAX_SEQUENCE_LEN)
strategy = strr
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def get_Char(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, get_Char, *args)

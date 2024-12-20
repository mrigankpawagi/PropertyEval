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
                
strr = text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=MAX_SEQUENCE_LEN)
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
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, get_Char, *args)

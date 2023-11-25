import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
s = text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=MAX_SEQUENCE_LEN)
strategy = s
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def word_len(s): 
    s = s.split(' ')   
    for word in s:    
        if len(word)%2!=0: 
            return True  
        else:
          return False

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, word_len, *args)

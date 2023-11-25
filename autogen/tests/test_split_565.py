import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
word = text(alphabet='abcdefghijklmnopqrstuvwxyz', max_size=MAX_SEQUENCE_LEN)
strategy = word
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def split(word): 
    return [char for char in word] 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, split, *args)

import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from string import ascii_lowercase, ascii_uppercase

def word():
    letters = list(ascii_lowercase) + list(ascii_uppercase)
    n = integers(min_value=1, max_value=MAX_SEQUENCE_LEN)
    return lists(sampled_from(letters), min_size=n, max_size=n).map(''.join)

strategy = word()
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def snake_to_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, snake_to_camel, *args)

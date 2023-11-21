import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
word = text(alphabet=string.ascii_lowercase, min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = word
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def snake_to_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, snake_to_camel, *args)

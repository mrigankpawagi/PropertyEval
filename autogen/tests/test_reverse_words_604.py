import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
s = text(alphabet=string.ascii_letters + string.digits + string.punctuation, min_size=1)
strategy = s,
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def reverse_words(s):
        return ' '.join(reversed(s.split()))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, reverse_words, *args)

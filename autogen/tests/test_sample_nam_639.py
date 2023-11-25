import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
import string
sample_names = lists(text(alphabet=string.ascii_letters, min_size=1), min_size=1)
strategy = sample_names
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sample_nam(sample_names):
  sample_names=list(filter(lambda el:el[0].isupper() and el[1:].islower(),sample_names))
  return len(''.join(sample_names))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, sample_nam, *args)

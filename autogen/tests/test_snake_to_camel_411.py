import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def snake_case_strings(draw):
    word = draw(text(alphabet=string.ascii_lowercase + '_', min_size=1))
    return word

word = snake_case_strings()

strategy = word
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def snake_to_camel(word):
  return ''.join(x.capitalize() or '_' for x in word.split('_'))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, snake_to_camel, *args)

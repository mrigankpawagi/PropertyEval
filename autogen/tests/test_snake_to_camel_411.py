import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
                
word = text(alphabet='abcdefghijklmnopqrstuvwxyz_', min_size=2, max_size=MAX_SEQUENCE_LEN).filter(lambda x: "_" in x)

strategy = word
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def snake_to_camel(word):
  return ''.join(x.capitalize() or '_' for x in word.split('_'))

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, snake_to_camel, *args)

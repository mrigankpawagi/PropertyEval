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
                
text = text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ', max_size=MAX_SEQUENCE_LEN)
pattern = text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ', max_size=MAX_SEQUENCE_LEN)

strategy = text, pattern
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re

def find_literals(text, pattern):
  match = re.search(pattern, text)
  s = match.start()
  e = match.end()
  return (match.re.pattern, s, e)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, find_literals, *args)

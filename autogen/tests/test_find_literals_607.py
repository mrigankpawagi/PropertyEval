import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
text_inp = text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', max_size=MAX_SEQUENCE_LEN)
pattern = text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', max_size=MAX_SEQUENCE_LEN)
strategy = text_inp, pattern
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re

def find_literals(text, pattern):
  match = re.search(pattern, text)
  s = match.start()
  e = match.end()
  return (match.re.pattern, s, e)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_literals, *args)

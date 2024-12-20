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
                
text1 = text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', min_size=0, max_size=MAX_SEQUENCE_LEN)
strategy = text1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def remove_whitespaces(text1):
  return (re.sub(r'\s+', '',text1))

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, remove_whitespaces, *args)

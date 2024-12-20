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
                
str1 = text(alphabet='abcdeABCDE', max_size=MAX_SEQUENCE_LEN).filter(lambda x: x == "" or x.islower())
strategy = str1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def remove_uppercase(str1):
  return re.sub('[A-Z]', '', str1)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, remove_uppercase, *args)

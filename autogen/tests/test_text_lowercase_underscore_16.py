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
                
text = text(alphabet='abcdefghijklmnopqrstuvwxyz_', min_size=2, max_size=MAX_SEQUENCE_LEN)
strategy = text
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def text_lowercase_underscore(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return True
        else:
                return False

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, text_lowercase_underscore, *args)

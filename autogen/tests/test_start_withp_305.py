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
                
words = lists(text(alphabet='Ppqrstuv', min_size=1), max_size=MAX_SEQUENCE_LEN)
strategy = words,
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def start_withp(words):
 for w in words:
        m = re.match("(P\w+)\W(P\w+)", w)
        if m:
            return m.groups()

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, start_withp, *args)

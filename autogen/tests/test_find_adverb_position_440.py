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
                
text = text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .', max_size=MAX_SEQUENCE_LEN)
strategy = text
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def find_adverb_position(text):
 for m in re.finditer(r"\w+ly", text):
    return (m.start(), m.end(), m.group(0))

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, find_adverb_position, *args)

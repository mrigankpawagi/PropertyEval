import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
                
import re

text = text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', max_size=MAX_SEQUENCE_LEN)
pattern = r'a+b+'
matches = from_regex(pattern).filter(lambda x: re.match(pattern, x) is not None)

strategy = text, matches
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def text_match_zero_one(text):
        patterns = 'ab+?'
        if re.search(patterns,  text):
                return True
        else:
                return False

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, text_match_zero_one, *args)

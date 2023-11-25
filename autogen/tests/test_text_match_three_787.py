import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
pattern = r'a{1}b{3}'
text = text(alphabet='abcdefghijklmnopqrstuvwxyz' + 'ab' * 100, max_size=MAX_SEQUENCE_LEN)
strategy = text, pattern
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def text_match_three(text):
        patterns = 'ab{3}?'
        return re.search(patterns,  text)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, text_match_three, *args)

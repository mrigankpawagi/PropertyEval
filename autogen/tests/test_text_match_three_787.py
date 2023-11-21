import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
import string

@composite
def create_text(draw):
    chars = string.ascii_lowercase
    n = draw(integers(min_value=0, max_value=MAX_SEQUENCE_LEN))
    text = ''.join(draw(sampled_from(chars)) for _ in range(n))
    return text

text = create_text().filter(lambda x: 'aaa' not in x)

strategy = text
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def text_match_three(text):
        patterns = 'ab{3}?'
        return re.search(patterns,  text)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, text_match_three, *args)

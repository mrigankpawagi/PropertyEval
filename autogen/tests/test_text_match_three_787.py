import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_text(draw):
    n = draw(integers(min_value=1, max_value=100))
    text = draw(text(alphabet='abcd', min_size=n, max_size=n))
    return text

text = create_text()

strategy = just(text),
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def text_match_three(text):
        patterns = 'ab{3}?'
        return re.search(patterns,  text)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, text_match_three, *args)

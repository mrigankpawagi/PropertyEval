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
    letters = draw(text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=10))
    word = draw(one_of(just('z'), letters))
    text = draw(just(word) | text())
    return text

text = create_text()

strategy = text
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def text_match_wordz_middle(text):
        return bool(re.search(r'\Bz\B',  text))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, text_match_wordz_middle, *args)

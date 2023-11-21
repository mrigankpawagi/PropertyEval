import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
text = text(alphabet=characters(min_codepoint=97, max_codepoint=122), min_size=1)

strategy = text
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def text_match_wordz_middle(text):
        return bool(re.search(r'\Bz\B',  text))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, text_match_wordz_middle, *args)

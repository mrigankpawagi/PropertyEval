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
                
text = text(alphabet='abcdefghijklmnopqrstuvwxyz ', max_size=100)
strategy = text,
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def text_match_wordz_middle(text):
        return bool(re.search(r'\Bz\B',  text))

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, text_match_wordz_middle, *args)

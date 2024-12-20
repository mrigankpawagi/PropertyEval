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
                
text = text(alphabet='abcd', min_size=4, max_size=20).filter(lambda x: 'abbb' in x)
strategy = text
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def text_match_three(text):
        patterns = 'ab{3}?'
        return re.search(patterns,  text)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, text_match_three, *args)

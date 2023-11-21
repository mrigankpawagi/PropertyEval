import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
text = text(alphabet='abcdefghijklmnopqrstuvwxyz ,', min_size=1, max_size=100)
pattern = text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=10)

strategy = text, pattern
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def occurance_substring(text,pattern):
 for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    return (text[s:e], s, e)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, occurance_substring, *args)

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
    prefix = draw(text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=0, max_size=10))
    suffix = draw(text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=10))
    return prefix + 'a' + suffix + 'b'

text = create_text()

strategy = text
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def text_starta_endb(text):
        patterns = 'a.*?b$'
        return re.search(patterns,  text)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, text_starta_endb, *args)

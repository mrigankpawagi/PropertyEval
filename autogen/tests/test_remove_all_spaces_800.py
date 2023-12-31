import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
text = text(min_size=1, max_size=MAX_SEQUENCE_LEN).map(lambda s: s.replace(" ", ""))
strategy = text
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def remove_all_spaces(text):
 return (re.sub(r'\s+', '',text))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, remove_all_spaces, *args)

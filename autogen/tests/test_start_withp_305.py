import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
words = lists(text(alphabet=string.ascii_letters + string.digits + string.punctuation, min_size=1), min_size=2)

def start_with_p(words):
    return [w for w in words if w.lower().startswith('p')]

strategy = words.map(start_with_p)
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def start_withp(words):
 for w in words:
        m = re.match("(P\w+)\W(P\w+)", w)
        if m:
            return m.groups()

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, start_withp, *args)

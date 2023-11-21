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
    n = draw(integers(min_value=1, max_value=10))
    text = draw(text(min_size=n, max_size=n))
    return text

text = create_text()

strategy = text
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def extract_values(text):
 return (re.findall(r'"(.*?)"', text))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, extract_values, *args)

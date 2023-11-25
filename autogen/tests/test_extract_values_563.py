import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
text = text()
strategy = text,
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def extract_values(text):
 return (re.findall(r'"(.*?)"', text))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, extract_values, *args)

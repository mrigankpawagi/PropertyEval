import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
text1 = text(alphabet=string.printable, min_size=1)
strategy = text1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def remove_whitespaces(text1):
  return (re.sub(r'\s+', '',text1))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, remove_whitespaces, *args)

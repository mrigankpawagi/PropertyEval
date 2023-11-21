import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
text = text()

strategy = text
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def replace_spaces(text):
  return "".join(" " if c == "_" else ("_" if c == " " else c) for c in text)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, replace_spaces, *args)

import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def extract_quotation_text(draw):
    text = draw(text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "', min_size=1, max_size=100))
    return text

text1 = extract_quotation_text()

strategy = text1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def extract_quotation(text1):
  return (re.findall(r'"(.*?)"', text1))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, extract_quotation, *args)

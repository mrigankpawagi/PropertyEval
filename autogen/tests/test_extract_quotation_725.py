import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_quoted_string(draw):
    n = draw(integers(min_value=1, max_value=10))
    strings = draw(lists(text(alphabet=characters(min_codepoint=32, max_codepoint=126), min_size=n, max_size=n), min_size=n, max_size=n))
    text = ' '.join(['"' + s + '"' for s in strings])
    return strings, text

def extract_quotation():
    strings, text = create_quoted_string()
    return text, strings

strategy = extract_quotation()
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def extract_quotation(text1):
  return (re.findall(r'"(.*?)"', text1))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, extract_quotation, *args)

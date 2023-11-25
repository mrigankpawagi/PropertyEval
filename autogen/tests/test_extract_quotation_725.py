import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
import re

@composite
def quotation_string(draw):
    text_inp = draw(text(alphabet="abc", max_size=MAX_SEQUENCE_LEN))
    # Generating random strings with quotation marks
    quo_str = ''.join(draw(text(alphabet='"', min_size=1, max_size=1)) + draw(text(min_size=1, max_size=10)) + draw(text(alphabet='"', min_size=1, max_size=1)) for _ in range(3))
    quo_str = re.sub(r'\s+', ' ', quo_str).strip()
    return text_inp + quo_str

strategy = quotation_string()
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def extract_quotation(text1):
  return (re.findall(r'"(.*?)"', text1))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, extract_quotation, *args)

import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from hypothesis import strategies as st

text = st.text(alphabet=st.characters(whitelist_categories=('Lu', 'Ll', 'Nd', 'Zs')));

strategy = text
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def find_adverbs(text):
  for m in re.finditer(r"\w+ly", text):
    return ('%d-%d: %s' % (m.start(), m.end(), m.group(0)))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_adverbs, *args)

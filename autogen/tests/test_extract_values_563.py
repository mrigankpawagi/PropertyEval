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
    values = draw(lists(text(min_size=1, alphabet=characters(blacklist_categories=('Cs', 'Cc', 'Pi', 'Pf'), whitelist_categories=('L', 'Z', 'P'))), min_size=1))
    quoted_values = [f'"{value}"' for value in values]
    text = ', '.join(quoted_values)
    return text

text = create_quoted_string()

strategy = text
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def extract_values(text):
 return (re.findall(r'"(.*?)"', text))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, extract_values, *args)

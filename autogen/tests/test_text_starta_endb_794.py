import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
import math
import string
                
import re

def text_starta_endb():
    return text(min_size=1, alphabet='ab').filter(lambda x: 'a' in x and x.endswith('b'))

strategy = text_starta_endb()
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def text_starta_endb(text):
        patterns = 'a.*?b$'
        return re.search(patterns,  text)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, text_starta_endb, *args)

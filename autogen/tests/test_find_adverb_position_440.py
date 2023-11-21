import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def adverb_position():
    adverbs = ["clearly", "seriously", "quickly", "easily"]
    adverb = sampled_from(adverbs)
    adverb_pos = integers(min_value=0)
    return (adverb_pos, adverb)

text = text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.', min_size=1)

strategy = adverb_position, text
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def find_adverb_position(text):
 for m in re.finditer(r"\w+ly", text):
    return (m.start(), m.end(), m.group(0))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_adverb_position, *args)

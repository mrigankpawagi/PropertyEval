import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
import string

@composite
def text_strategy(draw):
    n = draw(integers(min_value=0, max_value=100))
    letters = string.ascii_letters + string.digits + string.punctuation + ' '
    text = ''.join(draw(letters) for _ in range(n))
    return text

def find_adverb_position(text):
    words = text.split()
    for i, word in enumerate(words):
        if word.endswith('ly'):
            return 0, i, word
    return None

strategy = text_strategy().map(lambda text: (text,))
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def find_adverb_position(text):
 for m in re.finditer(r"\w+ly", text):
    return (m.start(), m.end(), m.group(0))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_adverb_position, *args)

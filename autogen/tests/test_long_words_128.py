import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_word_list(draw):
    n = draw(integers(min_value=0, max_value=10))
    word_list = draw(lists(text(alphabet=characters(min_codepoint=97, max_codepoint=122)),
                           min_size=n,
                           max_size=n))
    return word_list

n = integers(min_value=0, max_value=10)
word_list = create_word_list()

strategy = n, word_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, long_words, *args)

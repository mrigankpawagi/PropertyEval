import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=0, max_value=MAX_SEQUENCE_LEN)
words = lists(text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', min_size=1), max_size=MAX_SEQUENCE_LEN)

strategy = n, words
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

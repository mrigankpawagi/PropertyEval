import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
str1 = text(alphabet='abcdefghijklmnopqrstuvwxyz', max_size=MAX_SEQUENCE_LEN).filter(lambda x: x == "" or x.islower())

strategy = str1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def reverse_vowels(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, reverse_vowels, *args)

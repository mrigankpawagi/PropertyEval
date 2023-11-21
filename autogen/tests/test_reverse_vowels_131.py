import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def vowels():
    return one_of(just('a'), just('e'), just('i'), just('o'), just('u'), just('A'), just('E'), just('I'), just('O'), just('U'))

@composite
def consonants():
    return characters(blacklist_characters='aeiouAEIOUyY')

@composite
def build_strings_with_vowels():
    s = draw(text(alphabet=consonants(), min_size=1))
    v = draw(lists(vowels(), min_size=1))
    return s + ''.join(v)

@composite
def build_strings_without_vowels():
    s = draw(text(alphabet=consonants(), min_size=1))
    return s

str1 = st.one_of(build_strings_with_vowels(), build_strings_without_vowels())

strategy = strings
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

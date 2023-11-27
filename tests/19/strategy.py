from limits.limits import *
from hypothesis.strategies import lists, sampled_from

allowed_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

strategy = lists(sampled_from(allowed_words), max_size=MAX_SEQUENCE_LEN).map(lambda words: ' '.join(words))

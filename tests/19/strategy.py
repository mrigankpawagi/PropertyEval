from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import lists, sampled_from

allowed_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

strategy = lists(sampled_from(allowed_words), max_size=MAX_SEQUENCE_LEN).map(lambda words: ' '.join(words))

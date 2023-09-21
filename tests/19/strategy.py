from hypothesis.strategies import lists, sampled_from, integers

allowed_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
length = integers(min_value=0)

strategy = lists(sampled_from(allowed_words)).map(lambda words: ' '.join(words))

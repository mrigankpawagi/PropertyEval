from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN, SMALL_SEQUENCE_LEN
from hypothesis.strategies import lists, text, shared

list_of_strings = lists(text(alphabet='abcdefghij', max_size=SMALL_SEQUENCE_LEN), max_size=MAX_SEQUENCE_LEN)
lst1 = shared(list_of_strings)
lst2 = shared(list_of_strings)

strategy = lst1, lst2

from limits.limits import *
from hypothesis.strategies import sampled_from, lists

music_string = lists(sampled_from(["o", "o|", ".|"]), max_size=MAX_SEQUENCE_LEN).map(lambda s: " ".join(s))
                                            
strategy = music_string

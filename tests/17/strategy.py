import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import sampled_from, lists

music_string = lists(sampled_from(["o", "o|", ".|"]), max_size=MAX_SEQUENCE_LEN).map(lambda s: " ".join(s))
                                            
strategy = music_string

import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import builds, text, integers

def generate(d, m, y, sep):
    return f"{d}{sep}{m}{sep}{y}"

date = builds(generate, 
    integers(min_value=0, max_value=40), 
    integers(min_value=0, max_value=20), 
    integers(min_value=0, max_value=9999), 
    text(min_size=1, max_size=1, alphabet="/- ")
)

strategy = date

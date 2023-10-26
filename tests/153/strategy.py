import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import text, lists, builds

def join(s1, s2):
    return s1 + s2

class_name = builds(join, 
                    text(alphabet='abcdeFGHIJ_'),
                    text(alphabet='abcdeFGHIJ_01234'))

extensions = lists(builds(join, 
                        text(alphabet='abcdeFGHIJ_'),
                        text(alphabet='abcdeFGHIJ_01234')), min_size=1)

strategy = class_name, extensions

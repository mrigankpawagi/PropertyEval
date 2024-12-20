import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
import math
import string
                
subjectmarks = lists(tuples(text(), integers()), max_size=MAX_SEQUENCE_LEN)
strategy = subjectmarks
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def subject_marks(subjectmarks):
#subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])
 subjectmarks.sort(key = lambda x: x[1])
 return subjectmarks

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, subject_marks, *args)

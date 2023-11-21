import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
subjectmarks = lists(tuples(text(), integers()))

strategy = subjectmarks
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def subject_marks(subjectmarks):
#subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])
 subjectmarks.sort(key = lambda x: x[1])
 return subjectmarks

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, subject_marks, *args)

from limits.limits import *
from hypothesis.strategies import text

txt = text(alphabet='abcdeFGHIJ,. \n\t\r').filter(lambda s: not s.startswith(" ") and not s.startswith(",") and not s.endswith(" ") and not s.endswith(","))

strategy = txt

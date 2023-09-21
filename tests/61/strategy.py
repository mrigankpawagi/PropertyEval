# Ambiguous purpose statement
from hypothesis.strategies import text

brackets = text(alphabet="()")

strategy = brackets

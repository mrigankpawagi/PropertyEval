# Grount truth is incorrect! What about nan and inf?

from hypothesis.strategies import integers, floats

number = floats(min_value=0.0, exclude_min=True)

strategy = number

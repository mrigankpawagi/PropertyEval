# Groundtruth seems wrong because problem only stated "every opening bracket has a corresponding closing bracket" and not vice versa. (More like an ambiguity)

from hypothesis.strategies import text

brackets = text(alphabet="<>")

strategy = brackets

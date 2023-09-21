from hypothesis.strategies import integers, lists

operations = lists(integers(), max_size=5)

strategy = operations

from hypothesis.strategies import integers

number = integers(min_value=1, max_value=1000)

strategy = number

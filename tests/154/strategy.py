from hypothesis.strategies import text

a = text(alphabet='abc', max_size=10)
b = text(alphabet='abc', max_size=5)

strategy = a, b

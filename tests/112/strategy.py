from hypothesis.strategies import text

s = text(alphabet="abcdefghij", max_size=10)
c = text(alphabet="abcdefghij", max_size=5)

strategy = s, c

from hypothesis.strategies import text, integers

s = text(alphabet='abcdeABCDE ')
n = integers(min_value=0)

strategy = s, n

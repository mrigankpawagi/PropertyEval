from hypothesis.strategies import text

num = text(alphabet="0123456789ABCDEF")

strategy = num

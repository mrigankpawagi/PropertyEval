from hypothesis.strategies import text

s = text(alphabet=[chr(i) for i in range(32, 128)], max_size=10)

strategy = s

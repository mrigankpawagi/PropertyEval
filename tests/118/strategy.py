from hypothesis.strategies import text

word = text(alphabet='abcdeABCDE ').filter(lambda s: s.isalpha() or s == '')

strategy = word

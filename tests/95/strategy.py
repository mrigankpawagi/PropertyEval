from hypothesis.strategies import dictionaries, text

_dict = dictionaries(text(), text())

strategy = _dict

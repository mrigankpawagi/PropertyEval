from hypothesis.strategies import builds, floats

value = builds(str, floats())

strategy = value

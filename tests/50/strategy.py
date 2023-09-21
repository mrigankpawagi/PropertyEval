from hypothesis.strategies import text

s = text().filter(lambda x: x == "" or x.islower())

strategy = s

# This inherently has a roundabout property-based test

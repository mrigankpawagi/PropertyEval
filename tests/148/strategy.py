from hypothesis.strategies import sampled_from, text

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune",
           "Dummy1", "Dummy2", "Dummy3"]

planet1 = sampled_from(planets)
planet2 = sampled_from(planets)

strategy = planet1, planet2

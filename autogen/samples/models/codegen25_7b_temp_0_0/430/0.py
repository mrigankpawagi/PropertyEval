def parabola_directrix(a, b, c): 
  """
  Write a function to find the directrix of a parabola.
  """
  if a == 0:
    return "This is not a parabola"
  else:
    return (-b / (2 * a))

def parabola_vertex(a, b, c):
  """
  Write a function to find the vertex of a parabola.
  """
  if a ==
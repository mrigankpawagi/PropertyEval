def parabola_directrix(a, b, c): 
  """
  Write a function to find the directrix of a parabola.
  >>> parabola_directrix(5,3,2)==-198
  """
  return -b/(2*a)

def parabola_vertex(a, b, c):
  """
  Write a function to find the vertex of a parabola.
  >>> parabola_vertex(5,3,2)==-2
  """
  return -b/(2*a)
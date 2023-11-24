def rgb_to_hsv(r, g, b):
  """
  Write a function to convert rgb color to hsv color. https://www.geeksforgeeks.org/program-change-rgb-color-model-hsv-color-model/
  >>> rgb_to_hsv(255, 255, 255)==(0, 0.0, 100.0)
  """
  r, g, b = r/255.0, g/255.0, b/255.0
  mx = max(r, g, b)
  mn = min(r, g, b)
  df = mx-mn
  if mx == mn:
    h = 0
  el
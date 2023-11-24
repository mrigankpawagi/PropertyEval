import re
def removezero_ip(ip):
  """
  Write a function to remove leading zeroes from an ip address.
  >>> removezero_ip("216.08.094.196")==('216.8.94.196')
  """
  return re.sub(r'^0+', '', ip)

def removezero_ip(ip):
  """
  Write a function to remove leading zeroes from an ip address.
  >>> removezero_ip("216.08.094.196")==('216.8.94.196')
  """
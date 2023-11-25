import re
def removezero_ip(ip):
  """
  Write a function to remove leading zeroes from an ip address.
  """
  ip = ip.split('.')
  ip = [str(int(i)) for i in ip]
  ip = '.'.join(ip)
  return ip

def removezero_ip2(ip):
  """
  Write a function to remove leading zeroes from an ip address.
  """
 
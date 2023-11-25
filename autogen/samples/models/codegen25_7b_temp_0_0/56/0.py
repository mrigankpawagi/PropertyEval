def rev(num):    
    rev_num = 0
    while (num > 0):  
        rev_num = (rev_num * 10 + num % 10) 
        num = num // 10  
    return rev_num  
def check(n):    
  """
  Write a python function to check if a given number is one less than twice its reverse.
  """
  if n == rev(rev(n)):
    return True
  else:
    return False

def check_prime(n):
  """
  Write a python function to check if a given number is prime or not.
  """
  if n > 1:
    for i in range(2,n):
     
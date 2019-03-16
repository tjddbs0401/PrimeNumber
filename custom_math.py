import math
  
def isPrime(n): 
    result = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            result = False
            break
      
    return result

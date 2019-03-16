import math #math 사용
  
def isPrime(n): #isPrime()이라는 함수 정의
    result = True 
    for i in range(2, int(math.sqrt(n)) + 1): #소수라는 것이 판정되려면 그 숫자의 제곱근보다 작은 자연수들로 나눴을 때 안 나눠떨어지면 된다
        if n%i == 0:
            result = False #소수가 아니다
            break
      
    return result

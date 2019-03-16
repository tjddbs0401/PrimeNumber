import custom_math #custom_math.py에서 가져오기
count = input("Input: "); #n을 입력 받음
i = 2 
while 1 : #참일 때 계속 수행
    if(custom_math.isPrime(i)) : 
        count = count -1 
    if(count == 0): 
        break
    i = i+1
print("Number is =", i)

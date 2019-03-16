import custom_math 
count = input("Input: ");
i = 2 
while 1 : 
    if(custom_math.isPrime(i)) : 
        count = count -1
    if(count == 0): 
        break
    i = i+1
print("Number is =", i)

#素因数分解

N = int(input())

Limit = int(N ** 0.5)
divisor = []
primeFactor = []
result = 0

#Nの約数を取り出す
for i in range(1,Limit + 1):
    if N % i == 0:
        result = N // i 
        divisor.append(i)
        divisor.append(result)

divisor.sort()

#約数から素数のみ取り出す
for j in range(0,len(divisor)):
    priLim = int(divisor[j]**0.5)
    is_prime = True
    for k in range(2,priLim + 1):
        if divisor[j] % k ==0:
            is_prime = False
            break
    if is_prime:
        primeFactor.append(divisor[j])
        
#1は素数ではないので削除
primeFactor.pop(0)
print(primeFactor)


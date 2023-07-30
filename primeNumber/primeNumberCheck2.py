#素数判定
#計算量O(√N)
N = int(input())

Limit =int(N**0.5)

for i in range(2, Limit +1):
    if N % i ==0:
        print("No")
        break
    elif i == Limit :
        print("Yes")
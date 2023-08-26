#階乗の再帰関数
num = int(input())

def factorial(N):
    if N == 1:
        return N
    return N * factorial(N - 1)

print (factorial(num))

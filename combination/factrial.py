import math

#math.combi()
print("組み合わせの数を求めます")
n = int(input("全部の数　n="))
r = int(input("取り出す数　r="))
N = math.factorial(n)
leftover = math.factorial(n - r)
select = math.factorial(r)

answer = N // (leftover * select)

print(answer)
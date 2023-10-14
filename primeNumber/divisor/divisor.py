

#divisor 約数
N = int(input())
cnt = 0

for i in range(1, N + 1):
    if N % i == 0:
        print (i)
        cnt += 1
print('約数は'+ str(cnt) +'個')
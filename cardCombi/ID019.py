#mathモジュールを使わずに

N = int(input())
card = list(map(int,input().split()))

red = 0
yerrow = 0
blue = 0
ans = 0

def con2(n):
    return n * (n - 1) // 2

for i in range(N):
    if card[i] == 1:
        red += 1
    if card[i] == 2:
        yerrow += 1
    if card[i] == 3:
        blue += 1

ans =con2(red) +con2(yerrow) +con2(blue)

print (ans)
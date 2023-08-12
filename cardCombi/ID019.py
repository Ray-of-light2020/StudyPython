N = int(input())
card = list(map(int,input().split()))
import math

red = 0
yerrow = 0
blue = 0
ans = 0

for i in range(N):
    if card[i] == 1:
        red += 1
    if card[i] == 2:
        yerrow += 1
    if card[i] == 3:
        blue += 1

ans = math.comb(red,2) + math.comb(yerrow,2) + math.comb(blue,2)

print (ans)
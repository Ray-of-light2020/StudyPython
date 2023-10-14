N = int(input())
blue = map(list(int,input().split()))
red = map(list(int,input().split()))

bSum = 0
rSum  =0
bEx = 0
rEx = 0
ans = 0

for i in range(N):
    bSum += blue[i]
bEx = bSum // N

for j in range(N):
    rSum += red[j]
rEx = rSum // N

ans = bEx + rEx 

print (ans)


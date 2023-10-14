#N = int(input())
#blue = list(map(int,input().split()))
#red = list(map(int,input().split()))

N = int(6)
blue = [10,20,30,40,50,60]
red = [0,1,3,5,6,9]

ValSum = 0
ans = 0

for i in range(N):
    for j in range(N):
        ValSum = blue[i] + red[j]
        print (f"({ValSum})",end = "")
        ans += ValSum
    print ()


print (f"期待値は{ans // (N * N)}です。")
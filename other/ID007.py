N,X,Y = map(int,input().split())

cnt = 0
calcCnt = 0
for i in range(1,N + 1):
    calcCnt += 1
    if i % X == 0 or i % Y == 0:
            print (i)
            cnt += 1
print("計算回数は" + str(calcCnt) + "回")
print (str(N) + "以下" + str(X) + "の倍数" + str(Y)+"の倍数は"+str(cnt)+"個です。")


N = int(input("等の数？"))
eachAns = 0
ans = 0

for i in range(N):
    P = int(input("賞金？"))
    Q = float(input("確率？"))
    eachAns = P * Q
    ans += eachAns

print (ans)


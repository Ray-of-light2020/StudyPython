#選択式問題の試験をランダムに答えたときの期待値を求める。

N = int(input("問題数"))
P = list(map(int,input("各問題の選択肢の数を順番に問題数分を入力して下さい。").split()))
Q = list(map(int,input("各問題の得点を問題数分、順番に入力して下さい。").split()))

eachAns = 0
ans = 0

for i in range(N):
    eachAns = Q[i] // P[i]
    ans += eachAns

print(ans)

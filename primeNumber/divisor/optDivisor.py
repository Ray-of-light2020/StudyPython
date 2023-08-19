#約数を順に列挙します。
#計算回数は√N

N = int(input("約数を調べたい数字を入力して下さい。"))
A = []
limit = int(N ** 0.5)
divisor = 0
cnt = 0

for i in range(1,limit + 1):
    if N % i == 0:
        divisor =  N // i
        #重複を排除
        if divisor == i:
            A.append(i)
        else:
            A.append(divisor)
            A.append(i)
A.sort()
cnt = len(A)

for j in range(cnt):
    print(A[j])

print (f"約数は{cnt}個です。")
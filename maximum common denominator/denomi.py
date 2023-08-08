
#約数を表示します。
A,B = map(int,input().split())
mini = min(A,B)
res = []
for i in range(1,mini + 1):
    if A%i == 0 and B%i ==0:
        res.append(i)

print (f"約数は{res}です。")
maxCdenomi = max(res)
print (f"最大公約数は{maxCdenomi}です。")
#線形探索で最小値を検索

A = [5,6,3,1,3]
min = A[0]

for i in range(1,len(A)):
    if min > A[i]:
        min = A[i]
       
print (min)

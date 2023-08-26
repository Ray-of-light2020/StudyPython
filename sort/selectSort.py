
#選択ソート
A = [5,6,2,2,3]

for i in range(0,len(A)-1):
    min = i
    for j in range(i + 1,len(A)):
        if A[min] > A[j]:
            min = j
    #値をスワップ
    A[i],A[min] = A[min],A[i]
print(A)
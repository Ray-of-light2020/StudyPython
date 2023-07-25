N = int(input())

if N  > 10:
    print ("Nは10以下にして下さい")

if N <= 5:
    for i in range(5,1, -1):
        if i == N:
            print (N)
if N > 5:
    for i in range(5,11):
        if i == N:
            print (N)

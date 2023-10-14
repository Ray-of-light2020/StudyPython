A,B = map(int,input("最大公約数を求めます。").split())

while A >= 1 and B >= 1:
    if A < B:
        B = B % A 
    else:
        A = A % B

if A >= 1:
    print(A)
else:
    print(B)


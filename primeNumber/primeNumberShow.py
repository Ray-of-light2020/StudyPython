n = 286

lis = []

for i in range(2,n + 1):
    while True:
        if n%i == 0:
            lis.append(i)
            n = n//i    
            print(lis)
            print("n={}".format(n))
        else:
            break
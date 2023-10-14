N = int(input())
A = list(map(int, input().split()))

def f(idx, p, n):
    if n == 5:
        if p == 1000:
            return 1
        return 0
    
    res = 0
    for nidx in range(idx+1, N):
        res += f(nidx, p+A[nidx], n+1)
    
    return res

print(f(-1, 0, 0))
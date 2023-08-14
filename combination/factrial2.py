#mathモジュールを使わずに組み合わせを求める。
n,r = map(int,input().split())
ans = 0
def kaijou(x):
    result = 1
    for i in range(x,1,-1):
        result *= i
    return result

ans = kaijou(n) // (kaijou(r) * kaijou(n - r))

print(ans)
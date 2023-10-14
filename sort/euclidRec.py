#ユークリッド互除法を再帰関数で作成

A,B = map(int,input().split())

def GCD(A,B):
    if B == 0:
        return A
    return GCD(B, A%B)

print (GCD(A,B))
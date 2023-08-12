
#2つの同じ数字の組み合わせの数を数えます。

N = int(input())
card = list(map(int,input().split()))

if N == len(card):
    cnt = 0
    for i in range(0,N - 1):
        for j in range(i + 1,N):
            print(str(card[i]) + "," + str(card[j]))
            if card[i] == card[j]:
                cnt += 1

print (cnt)
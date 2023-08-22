#入力
N, Y = map(int, input().split())

#答えを格納するための変数
areas, bress, cres = -1, -1, -1

#全探索
for a in range(N+1):
    for b in range(N+1):
        #Cの値が自動的に決まる
        c = N - a - b
        
        #cが0以上n以下でない場合はスキップ
        if c < 0 or c > N:
            continue
        #残りの条件を満たすか判定
        if 10000 * a + 5000 * b + 1000 * c == Y:
            ares, bres, cres = a, b, c
#出力
print(areas, bres, cres)

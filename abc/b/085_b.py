#パケットのサイズ
M = 101

#入力のサイズ
N = int(input())

#バケット(全体を0で初期化)
exist = [0] * M

#N個の入力を受け取りながらバケットを作る
for i in range(N):
    d = int(input())
    
    #バケットを更新
    exist[d] = 1
    
#exist の総和を求めて出力する
print(sum(exist))



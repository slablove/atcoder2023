a, b = list(map(int, input().split()))

ans = -1 #答えが見つからなった場合の-1を初期値にしておく
#0円から9999円まで1円ずつ増やして調べる
for price in range(10000):
    tax_a = price * 8 // 100
    tax_b = price * 10 // 100
#条件を満たしたら答えに代入してループから抜ける
if tax_a == a and tax_b == b:
    ans = price
    #break
#答えが見つかったその時の値,見つからなかった初期値の-1が表示される
print(ans)






















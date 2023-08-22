# 入力の受け取り
Card=list(map(int,input().split()))
Card.sort()

# 1枚目と2枚目が同じ　かつ　3枚目と4枚目と5枚目が同じ
if Card[0]==Card[1] and Card[2]==Card[3]==Card[4]:
    # 「Yes」を出力
    print("Yes")
# 1枚目と2枚目と3枚目が同じ　かつ　4枚目と5枚目が同じ
elif Card[0]==Card[1]==Card[2] and Card[3]==Card[4]:
    # 「Yes」を出力
    print("Yes")
# どちらでもない
else:
    # 「No」を出力
    print("No")
    
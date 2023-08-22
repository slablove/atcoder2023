#入力の受け取り
P = list(map(int,input().split()))
#答えを格納する変数
ans = ""

#i=0~25
for i in range(26):
    #文字コードP[i]+96の文字をansの末尾へ追加
    ans+=chr(P[i]+96)
#答えを出力
print(ans)



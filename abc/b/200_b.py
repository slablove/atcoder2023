N , K = map(int,input().split()) 

for i in range(K): #for _ in range(K):
    if N%200 == 0:
        N = N//200 #N //= 200
    else:
        N = int(str(N) + "200")
print(N)

#整数 N が与えられます。
#以下の操作を K 回行った後の整数 N を出力してください。
#整数 N が 200 の倍数であれば、N を 200 で割る。
#そうでなければ、整数 N を、N の後ろに文字列として 200 を付け加えた整数に置き換える。
#例えば、7 を置き換えると 7200 に、1234 を置き換えると 1234200 になります。

#else: n = str(N) + "200"  N=int(n) print(N)
#else: n = int(str(n) + '200') print(n)
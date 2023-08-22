from re import X


#def time_3(x):
#    return 3*X


#入力の受け取り

t = int(input())


def f(x): #関数の定義
    return x**2+2*x+3 #引数:x 返り値 t^2+2t+3


#答えの計算
ans=f(f(f(t)+t)+f(f(t)))
#答えの出力
print(ans)

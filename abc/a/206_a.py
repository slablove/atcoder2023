# 入力の受け取り
N=int(input())

# 貯金額
money=0

# i=1~10**6
for i in range(1,10**6):
    # i日目　i円を貯金箱へ
    money+=i
    # 貯金額がN以上ならば
    if N<=money:
        # iを出力
        print(i)
        # 終了
        exit() #break

#N = int(input())
#ans = 0
#for i in range(1,10**9):
# ans+=i
# if ans>=N:
#   print(i)
#   exit()

#i日目に貯金箱へいくら入っているか、for文で1日ずつ実際に計算すればOKです。
#貯金額がN以上となった時点で「i」を出力し、プログラムを終了します。(exit()で終了できます)
#import math
#n = int(input())
#x = (-1 + (1+8*n)**(1/2))/2
#if x == int(x):
#    print(math.floor(x))
#else:
#    print(math.floor(int(x)+1))


#from math import sqrt
#from math import ceil
#n = int(input())
#answer = -0.5 + sqrt(1+8*n)/2.0
#print(ceil(answer))

#import math
#n = int(input())
#y_root = math.sqrt(1 + (8 * n))
#ans = (y_root - 1) / 2
#print(math.ceil(ans))

#n = int(input())
# def total(d):
#   return(d+1) * d // 2
#bottom = 0
#d = 1
#while total(d)< n:
# d += 1
#print(d)
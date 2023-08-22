N = int(input())

print((N + 1) // 2)

#偶数ページの場合は、2で割った枚数、奇数ページの場合は、もう1枚必要になります。
#2で割った値に余りがあれば1足す感じです。先に1足してから割ってもOKです。
#print(int(n // 2) if n % 2 == 0 else int(n // 2 + 1))
#ans = n//2 if n%2 != 0:  ans += 1 print(ans)s
#import math n = int(input()) ans = math.ceil(n/2) print(ans)
#n = int(input()) ans = -(-n//2) print(ans)

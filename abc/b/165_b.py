import math

x = int(input())

yen = 100
count = 0

while yen < x:
    count = count+1
    yen = math.floor(yen*1.01) #math.floor() 小数点以下を切り捨て


print(count)

#while yen < x: yen = yen*1.01//1 count += 1 print(count)
#while True: if yen >= x: break m = int(m*1.01) ans += 1 print(ans)

#x = int(input())
#n = 1000
#ans = 0
#while n<x:
#    n = int(n*1.01)
#    ans += 1
#print(ans)
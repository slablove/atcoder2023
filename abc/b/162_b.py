N = int(input())

result = 0
for i in range(1,N+1):
    if i % 3 == 0 or i % 5 == 0:
        continue
    result += i
print(result)

#if i%3 != 0 and i%5 != 0: ans += i print(ans)
#count = 0 n = int(input()) for i in range(1,n+1): if i %3 and i%5: count += i print(count)
#3でも5でも割り切れない総和を求める
#print(sum([x for x in range(1, int(input() + 1) if (x%3!=0) and (x%5!=0))]))

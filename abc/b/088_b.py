n = int(input())
l = list(map(int,input().split()))

a=b=0

l.sort(reverse=True)

for i in range(len(l)):
    if i%2==0:
        a+=l[i]
    else:
        b+=l[i]
print(a-b)

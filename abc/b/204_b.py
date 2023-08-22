n = int(input())
count = 0

for i in range(n):
    a = map(int,input().split())
    if a[i]>10:
        count = a[i] -10 
    else:
        count = 0
print(count)

#204正答

n = int(input())
a = list(map(int,input().split())) #1 2 3 4 5 6 7~
#答え
ans = 0
for i in range(n):        #A[i]が10より大きければ
    if a[i]>10:            #A[i]-10をansにプラスする
        ans+=a[i]-10 #ans = ans +a[i]-10
print(ans)
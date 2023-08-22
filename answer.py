n=int(input())
count = 0
for i in range(n):
	d = list(map(int,input().split()))
if d[i] == d[i+1]:
            count += 1

if count >=3:
    print("Yes")
else:
    print("No")
    









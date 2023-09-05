k = int(input())
count=0
ans="No"
for i in range(k):
  a,b = map(int,input().split())
  if a == b:
    count += 1
  else:
    count = 0
  if count == 3:
    ans="Yes"
print(ans)

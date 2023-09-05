k = int(input())
count=0
for i in range(k):
  a,b = map(int,input().split())
  if a == b:
    count += 1
if count >= 3:
  print("Yes")
else:
  print("No")

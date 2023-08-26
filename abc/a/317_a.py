n = int(input())
n,h,x= map(int,input().split())
p = list(map(int,input().split()))
q = []

for i in range(n):
  if h + p[i] >= x:
    q.append(p[i])
t = min(q)

print(p.index(t)+1)

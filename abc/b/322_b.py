n,m=map(int,input().split())

s=input()
t=input()

ans=0

if t[:n]!=s:
  ans+=2
  
if t[-n:]!=s:
  ans+=1
  
print(ans)

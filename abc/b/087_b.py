a = int(input())
b = int(input())
c = int(input())
x = int(input())
count = 0

for i in range(a+1):
  for j in range(b+1):
    for k in range(c+1):
      if i*500 + j*100 + k*50 == x:
        count+=1

print(count)

#a,b,c,x=map(int,open(0))
#print(sum(500*i+100*j+50*k==x for i in range(a+1)for j in range(b+1)for k in range(c+1)))

#a = int(input())
#b = int(input())
#c = int(input())
#x = int(input())

#ans = 0

#for i in range(a+1):
# for j in range(b+1):
#    for k in range(c+1):
#      if (500 * i + 100 * j + 50 * k == x):
#        ans += 1

#print(ans)
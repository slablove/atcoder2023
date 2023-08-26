n = int(input())
a = list(map(int,input().split()))
b = sorted(a)
print(sum(list(range(b[0],b[-1]+1)))-sum(b))

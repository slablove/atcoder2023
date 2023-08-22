N = int(input())
A = int(input())

print('Yes' if N%500 <= A else 'No')

#ちょうどN円を支払えるという条件を上手に言い換える
#mod = N % 500 if mod<=A: print("Yes") else: print("No")
